# CODEGUARDIAN

This Visual Studio Code extension allows you to use the [Azure OpenAI Studio API](https://azure.microsoft.com/en-us/products/ai-services/openai-service) to scan the code in your editor for potential security vulnerabilities. The extension will highlight any potential vulnerabilities in the code using [GPT4](https://openai.com/product/gpt-4)-based models.

## Features
- 🖱️ Right click on a code selection and run one of the context menu **shortcuts**
	- Scan for **security vulnerabilities**
- 💻 View GPT4's responses in a panel next to the editor
- 🚀 See the response as it is being generated **in real time**

## Note

> **Status**: This extension was confirmed working and tested as of **August 2024**.

## Setup

To use this extension, we need to build it from source at the moment. This is because the extension is not yet available on the Visual Studio Code marketplace.

To build the extension from source, clone the repository and run `npm install` to install the dependencies.


### Setting up Azure OpenAI Studio for API key

To use this extension, you need an API key from Azure OpenAI Studio. First, you must create Azure OpenAI via `Azure AI services ` -> Click `+ Create`. Please check regions for certain GPT models' availability (CODEGUARDIAN has been only tested with GPT-4-based models, such as GPT-4 Turbo and GPT-4o). 

After creating the resource, you can find the API key and the Endoint URL in the `Keys and Endpoint` section of the resource.

Furthermore, you need to create a deployment for the resource. You can do this by clicking on the `Go to Azure OpenAI Studio` and then clicking on the `Deployments` tab in the resource and clicking `+ New Deployment`.

Please note that the API key may take a few minutes to become active. If you try to use the API key too soon, you may receive an error message like:
`The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.`


### Setting up the extension

After you have cloned the repository and installed the dependencies (i.e., run `npm install webpack webpack-dev-server --save-dev`), you need to set up the extension in VScode debugger at the moment. Open `src/extension.ts` and press `F5` or navigate to the `Run` tab and click `Start Debugging`.

NOTE: If you change th extension code, you need to re-complie the extension by running `npm run compile` and then restarting the debugger.

### Settings

You must set your Azure OpenAI Studio API key to`Api Key`, your endpoint to `Api Url`, and your deployment name/id to `Deployment Id`, respectively. You can open the setting by clicking on the gear icon in the CODEGUARDIAN debugger panel and then search `code_guardian`. You may need to refresh the debugger panel to see the changes by ctl+R or command+R (for Mac). 

## Using the Extension

To use the extension, open your code in the debugger's editor. You can open the CODEGUARDIAN panel by clicking on the CODEGUARDIAN icon (guardman standing in front of a house) in the sidebar. This allow you to see the responses from the AI as they are generated.

You can right-click and select "Code-Guardian: CWE scan". The **selected code will be automatically appended** to your query when it is sent to the AI.


#### Commands:
- `Code-Guardian: CWE scan`


Please note that this extension is currently a proof of concept and may have some limitations or bugs. If you encounter any issues, please open an issue on the GitHub repository.


## Credits

- This respository is branched from [timkmecl / chatgpt-vscode](https://github.com/timkmecl/chatgpt-vscode)