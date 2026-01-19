import * as vscode from 'vscode';
import { ChatGPTAPI } from 'chatgpt'; // Source: https://github.com/transitive-bullshit/chatgpt-api
import { OpenAIClient, AzureKeyCredential, ChatRequestMessageUnion } from "@azure/openai";
import { prompts } from "./prompts";

type AuthInfo = {apiKey?: string};
type Settings = {selectedInsideCodeblock?: boolean, codeblockWithLanguageId?: false, pasteOnClick?: boolean, keepConversation?: boolean, timeoutLength?: number, model?: string, apiUrl?: string, deploymentId?: string};

export function activate(context: vscode.ExtensionContext) {

	console.log('activating extension "Code-Guardian"');
	// Get the settings from the extension's configuration
	const config = vscode.workspace.getConfiguration('code_guardian');
	console.log("Config: ", config);

	// Create a new ChatGPTViewProvider instance and register it with the extension's context
	const provider = new ChatGPTViewProvider(context.extensionUri);

	// Put configuration settings into the provider
	provider.setAuthenticationInfo({
		apiKey: config.get('apiKey')
	});
	provider.setSettings({
		selectedInsideCodeblock: config.get('selectedInsideCodeblock') || false,
		codeblockWithLanguageId: config.get('codeblockWithLanguageId') || false,
		pasteOnClick: config.get('pasteOnClick') || false,
		keepConversation: config.get('keepConversation') || false, // Make it false laterrrr //
		timeoutLength: config.get('timeoutLength') || 60,
		apiUrl: config.get('apiUrl'),
		// model: 'gpt-4-turbo'
		deploymentId: config.get('deploymentId'),
		model: config.get('model')
	});

	// DEBUG: output the settings of apiUrl and deploymentId
	console.log("API URL: ", config.get('apiUrl'));
	console.log("Deployment ID: ", config.get('deploymentId'));

	// Register the provider with the extension's context
	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(ChatGPTViewProvider.viewType, provider,  {
			webviewOptions: { retainContextWhenHidden: true }
		})
	);

	// For cweScan, we must run another function from the provider
	const commandHandler_cweScan = (command:string) => {
		const config = vscode.workspace.getConfiguration('code_guardian');
		const prompt = config.get(command) as string;
		provider.cweScan(prompt);
	}

	// Register the commands that can be called from the extension's package.json
	context.subscriptions.push(
		// Test command for our project
		vscode.commands.registerCommand('chatgpt.cweScan', () => commandHandler_cweScan('promptPrefix.cweScan')),
		vscode.commands.registerCommand('chatgpt.resetConversation', () => provider.resetConversation())
	);

	// Change the extension's session token or settings when configuration is changed
	vscode.workspace.onDidChangeConfiguration((event: vscode.ConfigurationChangeEvent) => {
		if (event.affectsConfiguration('chatgpt.apiKey')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setAuthenticationInfo({apiKey: config.get('apiKey')});
		}else if (event.affectsConfiguration('chatgpt.apiUrl')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			let url = config.get('apiUrl')as string;
			provider.setSettings({ apiUrl: url });
		} else if (event.affectsConfiguration('chatgpt.model')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ model: config.get('model') || 'gpt-3.5-turbo' }); 
		} else if (event.affectsConfiguration('chatgpt.selectedInsideCodeblock')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ selectedInsideCodeblock: config.get('selectedInsideCodeblock') || false });
		} else if (event.affectsConfiguration('chatgpt.codeblockWithLanguageId')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ codeblockWithLanguageId: config.get('codeblockWithLanguageId') || false });
		} else if (event.affectsConfiguration('chatgpt.pasteOnClick')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ pasteOnClick: config.get('pasteOnClick') || false });
		} else if (event.affectsConfiguration('chatgpt.keepConversation')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ keepConversation: config.get('keepConversation') || false });
		} else if (event.affectsConfiguration('chatgpt.timeoutLength')) {
			const config = vscode.workspace.getConfiguration('code_guardian');
			provider.setSettings({ timeoutLength: config.get('timeoutLength') || 60 });
		}
	});
}



class ChatGPTViewProvider implements vscode.WebviewViewProvider {
	public static readonly viewType = 'chatgpt.chatView';
	private _view?: vscode.WebviewView;

	private _chatGPTAPI?: OpenAIClient;
	private _conversation?: any;
	private _deploymentId? : string;

	private _response?: string;
	private _prompt?: string;
	private _system_prompt?: string;
	private _prompt_for_binary?: string;
	private _prompt_for_cwe?: string;
	private _fullPrompt?: string;
	private _fullPrompt_binary?: string;
	private _fullPrompt_cwe?: string;
	private _currentMessageNumber = 0;

	private _settings: Settings = {
		selectedInsideCodeblock: false,
		codeblockWithLanguageId: false,
		pasteOnClick: true,
		keepConversation: true,
		timeoutLength: 60,
	};
	private _authInfo?: AuthInfo;

	// Conversation history is stored as an array of objects with the following structure:
	private _conversationHistory: { prompt: string; response: string }[] = [];
	private _conversationHistory_cwe: { classification_type: string; response: string }[] = [];


	// In the constructor, we store the URI of the extension
	constructor(private readonly _extensionUri: vscode.Uri) {

	}
	
	// Set the API key and create a new API instance based on this key
	public setAuthenticationInfo(authInfo: AuthInfo) {
		this._authInfo = authInfo;
		this._newAPI();
	}

	public setSettings(settings: Settings) {
		let changeModel = false;
		if (settings.apiUrl || settings.model) {
			changeModel = true;
		}
		this._settings = {...this._settings, ...settings};

		if (changeModel) {
			this._newAPI();
		}
	}

	public getSettings() {
		return this._settings;
	}

	private _newAPI() {
		console.log("New API");
		if (!this._authInfo || !this._settings?.apiUrl) {
			console.warn("API key or API URL not set, please go to extension settings (read README.md for more info)");
		}else{
			const endpoint = this._settings.apiUrl;
			const azureApiKey = this._authInfo.apiKey || "xx";
			this._chatGPTAPI = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
			console.log( this._chatGPTAPI );
		}
	}

	// This method is called when the webview is created
	public resolveWebviewView(
		webviewView: vscode.WebviewView,
		context: vscode.WebviewViewResolveContext,
		_token: vscode.CancellationToken,
	) {
		this._view = webviewView;

		// set options for the webview, allow scripts
		webviewView.webview.options = {
			enableScripts: true,
			localResourceRoots: [
				this._extensionUri
			]
		};

		// set the HTML for the webview
		webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);

		// add an event listener for messages received by the webview
		webviewView.webview.onDidReceiveMessage(data => {
			switch (data.type) {
				case 'codeSelected':
					{
						// do nothing if the pasteOnClick option is disabled
						if (!this._settings.pasteOnClick) {
							break;
						}
						let code = data.value;
						const snippet = new vscode.SnippetString();
						snippet.appendText(code);
						// insert the code as a snippet into the active text editor
						vscode.window.activeTextEditor?.insertSnippet(snippet);
						break;
					}
				case 'prompt':
					{
						this.cweScan(data.value);
					}
			}
		});
	}


	public async resetConversation() {
		console.log(this, this._conversation);
		if (this._conversation) {
			this._conversation = null;
		}
		this._prompt = '';
		this._response = '';
		this._fullPrompt = '';
		this._view?.webview.postMessage({ type: 'setPrompt', value: '' });
		this._view?.webview.postMessage({ type: 'addResponse', value: '' });
	}

	// This method is called when the cweScan command is called
	public async cweScan(prompt?:string) {
		this._view?.webview.postMessage({ type: 'addResponse', value: '...' });

		this._system_prompt = prompts.system_prompt
		this._prompt_for_binary = prompts.binary
		this._prompt_for_cwe = prompts.cwe
		console.log("Running cwe Scan with the cascade setting!");

		// Check if the ChatGPTAPI instance is defined
		if (!this._chatGPTAPI) {
			this._newAPI();
		}

		// focus gpt activity from activity bar
		if (!this._view) {
			await vscode.commands.executeCommand('chatgpt.chatView.focus');
		} else {
			this._view?.show?.(true);
		}
		
		// Call updateConversationHistory to update the webview with the conversation history
		this._view?.webview.postMessage({ type: 'updateConversationHistoryCWE', value: this._conversationHistory_cwe});


		let response = '';
		let response_binary = '';
		this._response = '';
		// Get the selected text of the active editor
		const selection = vscode.window.activeTextEditor?.selection;
		const selectedText = vscode.window.activeTextEditor?.document.getText(selection);
		// Get the language id of the selected text of the active editor
		// If a user does not want to append this information to their prompt, leave it as an empty string
		const languageId = (this._settings.codeblockWithLanguageId ? vscode.window.activeTextEditor?.document?.languageId : undefined) || "";
		let searchPrompt_binary = '';
		let searchPrompt_cwe = '';

		if (selection && selectedText) {
			// If there is a selection, add the prompt and the selected text to the search prompts
			if (this._settings.selectedInsideCodeblock) {
				searchPrompt_binary = `${this._prompt_for_binary}\n\`\`\`${languageId}\n${selectedText}\n\`\`\``;
				searchPrompt_cwe = `${this._prompt_for_cwe}\n\`\`\`${languageId}\n${selectedText}\n\`\`\``;
			} else {
				searchPrompt_binary = `${this._prompt_for_binary}\n${selectedText}\n`;
				searchPrompt_cwe = `${this._prompt_for_cwe}\n${selectedText}\n`;
			}
		} else {
			// Otherwise, just use the prompt if user typed it
			searchPrompt_binary = this._prompt_for_binary
			searchPrompt_cwe = this._prompt_for_cwe
		}
		this._fullPrompt_binary = searchPrompt_binary;
		this._fullPrompt_cwe = searchPrompt_cwe;
		
		// Assign 
		const messages_binary: ChatRequestMessageUnion[] = [
			{ role: "system", content: this._system_prompt },
			{ role: "user", content: searchPrompt_binary },
		];
		const messages_cwe: ChatRequestMessageUnion[] = [
			{ role: "system", content: this._system_prompt },
			{ role: "user", content: searchPrompt_cwe },
		];

		// Increment the message number
		this._currentMessageNumber++;
		let currentMessageNumber = this._currentMessageNumber;
		let accumulator_biinary = "";
		let accumulator_cwe = "";

		if (!this._chatGPTAPI) {
			response = '[ERROR] "API key not set or wrong, please go to extension settings to set it (read README.md for more info)"';
		} else {
			// If successfully signed in
			console.log("sendMessage");
			
			// Make sure the prompt is shown
			this._view?.webview.postMessage({ type: 'setPrompt', value: 'Run CWE-scan' });

			const agent = this._chatGPTAPI;
			this._deploymentId = this._settings.deploymentId || "";

			try {
				const res_binary = await agent.streamChatCompletions(
					this._deploymentId,
					messages_binary,
					{ temperature: 0.1 }
				);

				// This is the code to get the response from the streamChatCompletions
				for await (const message of res_binary) {
					if ( message.choices && message.choices.length > 0) {
						const choice = message.choices[0];
					  	if (choice.delta && choice.delta.content) {
							// console.log(choice.delta.content);
							accumulator_biinary += choice.delta.content;
						}
					}
				}

				response_binary = accumulator_biinary;
				console.log("Response from binary scan: ", response_binary);

				// if the response_binary contains the word "not vulnerable", then we don't need to run the cwe scan
				// else, we run the cwe scan
				if (response_binary.includes("not vulnerable")) {
					response_binary = `The provided code is not vulnerable. Thus, no need to run the CWE scan.<br><br>\n\n---\n`;

					this._view?.webview.postMessage({ type: 'addResponse', value: response_binary });
					
					// Saves the response
					this._conversationHistory_cwe.push({ classification_type: 'binary', response: response_binary });
				} else {
					// First, we push the response from the binary scan
					response_binary = `The provided code is vulnerable! Thus, let's run the further CWE analysis.`;
					// this._conversationHistory_cwe.push({ classification_type: 'binary', response: response_binary });
					
					// Send the search prompt to the ChatGPTAPI instance and store the response
					const res = await agent.streamChatCompletions(
						this._deploymentId,
						messages_cwe,
						{ temperature: 0.1 }
					);
	
					// This is the code to get the response from the streamChatCompletions
					for await (const message of res) {
						if ( message.choices && message.choices.length > 0) {
							const choice = message.choices[0];
							  if (choice.delta && choice.delta.content) {
								// console.log(choice.delta.content);
								accumulator_cwe += choice.delta.content;
								// Show the view and send a message to the webview with the latest response
								if (this._view && this._view.visible) {
									this._view.webview.postMessage({ type: 'addResponse', value: `The provided code is vulnerable! Thus, let's run the further CWE analysis.<br><br>${accumulator_cwe}` });
								}
							}
						}
					}

					console.log("Response from cwe scan: ", accumulator_cwe);

					response = accumulator_cwe;
					response += `<br><br>\n\n---\n`;
					
					// Saves the response
					this._conversationHistory_cwe.push({ classification_type: 'cwe', response: `The provided code is vulnerable! Thus, let's run the further CWE analysis.<br><br>${response}` });
				};

				if (this._currentMessageNumber !== currentMessageNumber) {
					console.log("Message number changed");
					return;
				}

			} catch (e:any) {
				console.error(e);
				if (this._currentMessageNumber === currentMessageNumber){
					response = this._response;
					response += `\n\n---\n[ERROR] ${e}`;
				}
			}
		}

		if (this._currentMessageNumber !== currentMessageNumber) {
			console.log("Message number changed");
			return;
		}

		// Saves the response
		this._response = response;
	}

	
	
	// This method is called when the webview is created - thus, only once
	private _getHtmlForWebview(webview: vscode.Webview) {

		const scriptUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, 'media', 'main.js'));
		const microlightUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, 'media', 'scripts', 'microlight.min.js'));
		const tailwindUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, 'media', 'scripts', 'showdown.min.js'));
		const showdownUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, 'media', 'scripts', 'tailwind.min.js'));

		return `<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<script src="${tailwindUri}"></script>
				<script src="${showdownUri}"></script>
				<script src="${microlightUri}"></script>
				<style>
					.code {
						white-space: pre;
					}
					p {
						padding-top: 0.3rem;
						padding-bottom: 0.3rem;
					}
					/* overrides vscodes style reset, displays as if inside web browser */
					ul, ol {
						list-style: initial !important;
						margin-left: 10px !important;
					}
					h1, h2, h3, h4, h5, h6 {
						font-weight: bold !important;
					}
					#main-content {
						/* Take the full height minus the height of the input container */
						height: calc(100vh - 5rem); /* Adjust the 2.5rem to match your input container's total height */
						/* Make it scrollable */
						overflow-y: auto;
					}
					
					#text-box {
						height: 2.5rem; /* Fixed height */
						background-color: #4a5568; /* Existing background color */
						color: rgba(255, 255, 255, 0.6); /* Lighter white, similar to a placeholder */
						display: flex;
						align-items: center;
						justify-content: flex-start; /* Aligns content to the left */
						font-size: 0.9rem;
						padding: 0.5rem 1rem; /* Adjust padding as needed */
						white-space: nowrap;
						overflow: auto; /* Enable scrolling for overflow */
						min-width: 0; /* Allows the box to shrink with the viewport, consider adjusting based on your layout */
					}
					</style>
			</head>
			<body>
				<div id="main-content" class="pb-0 overflow-auto">
					<div id="conversation-history" class="pt-4 text-sm"></div>
					<div id="prompt-text" class="pt-4 text-sm"></div>
					<div id="response" class="pt-4 text-sm pb-"></div>
				</div>
				<div id="input-container" class="fixed bottom-0 left-0 w-full px-4 pb-5 word-wrap: break-word">
                	<div id="text-box">Highlight code and right click to "Code-Guardian: CWE scan"</div>
            	</div>
				<script src="${scriptUri}"></script>
			</body>
			</html>`;
	}
}

// This method is called when your extension is deactivated
export function deactivate() {}