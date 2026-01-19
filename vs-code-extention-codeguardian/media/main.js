// @ts-ignore 

// This script will be run within the webview itself
// It cannot access the main VS Code APIs directly.
(function () {
  const vscode = acquireVsCodeApi();

  let response = '';

  // Handle messages sent from the extension to the webview
  window.addEventListener("message", (event) => {
    const message = event.data;
    switch (message.type) {
      case "addResponse": {
        response = message.value;
        setResponse(); // OLD CODE
        // appendNewContent(response); // NEW CODE
        // updateConversation(response); // NEW CODE
        break;
      }
      case "clearResponse": {
        response = '';
        break;
      }
      case "setPrompt": {
        setPrompt(message.value);
        break;
      }
      case 'updateConversationHistory': {
        console.log('Received conversation history');
        // const conversationHistory = JSON.parse(message.value); // Deserializing the string back to an array
        updateConversationHistory(message.value);
        break;
      }
      case 'updateConversationHistoryCWE': {
        console.log('Received conversation history for CWE');
        // const conversationHistoryCWE = JSON.parse(message.value); // Deserializing the string back to an array
        updateConversationHistoryCWE(message.value);
        break;
      }
    }    
  });

  function fixCodeBlocks(response) {
    /* Ensure that if there's an odd number of triple backtick sequences (```), indicating code blocks, 
    an extra sequence is appended to the end. This ensures all code blocks are properly closed. */

    // Use a regular expression to find all occurrences of the substring in the string
    const REGEX_CODEBLOCK = new RegExp('\`\`\`', 'g');
    const matches = response.match(REGEX_CODEBLOCK);

    // Return the number of occurrences of the substring in the response, check if even
    const count = matches ? matches.length : 0;
    if (count % 2 === 0) {
      return response;
    } else {
      // else append ``` to the end to make the last code block complete
      return response.concat('\n\`\`\`');
    }

  }

  function setResponse() {
        // Initialize the showdown converter
        var converter = new showdown.Converter({
          omitExtraWLInCodeBlocks: true, 
          simplifiedAutoLink: true,
          excludeTrailingPunctuationFromURLs: true,
          literalMidWordUnderscores: true,
          simpleLineBreaks: true
        });
        response = fixCodeBlocks(response);
        // Convert the response to HTML, such as omits extra white space in code blocks
        html = converter.makeHtml(response);
        html = converter.makeHtml(`**Response:** ${response}`);
        document.getElementById("response").innerHTML = html;

        var preCodeBlocks = document.querySelectorAll("pre code");
        for (var i = 0; i < preCodeBlocks.length; i++) {
            preCodeBlocks[i].classList.add(
              "p-2",
              "my-2",
              "block",
              "overflow-x-scroll"
            );
        }
        
        var codeBlocks = document.querySelectorAll('code');
        for (var i = 0; i < codeBlocks.length; i++) {
            // Check if innertext starts with "Copy code"
            if (codeBlocks[i].innerText.startsWith("Copy code")) {
                codeBlocks[i].innerText = codeBlocks[i].innerText.replace("Copy code", "");
            }

            codeBlocks[i].classList.add("inline-flex", "max-w-full", "overflow-hidden", "rounded-sm", "cursor-pointer");

            codeBlocks[i].addEventListener('click', function (e) {
                e.preventDefault();
                vscode.postMessage({
                    type: 'codeSelected',
                    value: this.innerText
                });
            });

            const d = document.createElement('div');
            d.innerHTML = codeBlocks[i].innerHTML;
            codeBlocks[i].innerHTML = null;
            codeBlocks[i].appendChild(d);
            d.classList.add("code");
        }

        microlight.reset('code');

        //document.getElementById("response").innerHTML = document.getElementById("response").innerHTML.replaceAll('<', '&lt;').replaceAll('>', '&gt;');
  }

function updateConversationHistory(conversationHistory) {
  // Initialize the showdown converter
  var converter = new showdown.Converter({
      omitExtraWLInCodeBlocks: true, 
      simplifiedAutoLink: true,
      excludeTrailingPunctuationFromURLs: true,
      literalMidWordUnderscores: true,
      simpleLineBreaks: true
  });

  // Convert each conversation object into a markdown string
  var markdown = conversationHistory.map(convo => {
    return `<br>**Prompt:** ${fixCodeBlocks(convo.prompt)}<br><br>**Response:** ${fixCodeBlocks(convo.response)}`;
  }).join('');

  // Convert the markdown string to HTML
  var html = converter.makeHtml(markdown);
  document.getElementById("conversation-history").innerHTML = html;
}

// This is especially for the cascade scan (cweScan)  
function updateConversationHistoryCWE(conversationHistoryCWE) {
  // Initialize the showdown converter
  var converter = new showdown.Converter({
      omitExtraWLInCodeBlocks: true, 
      simplifiedAutoLink: true,
      excludeTrailingPunctuationFromURLs: true,
      literalMidWordUnderscores: true,
      simpleLineBreaks: true
  });

  // Filter conversation objects with classification_type "cwe" and convert to a markdown string
  var markdown = conversationHistoryCWE.map(convo => {
    return `<br>**You:** Run CWE-scan<br><br>**Response:** ${fixCodeBlocks(convo.response)}`;
  }).join('');

  // Convert the markdown string to HTML
  var html = converter.makeHtml(markdown);
  document.getElementById("conversation-history").innerHTML = html;
}


// Function to show the current prompt in webview for the "prompt" div id.
function setPrompt(prompt) {
  // TODO: Set the prompt in the webview. Add the `**Prompt:**` prefix to the prompt string.

  // Initialize the showdown converter
  var converter = new showdown.Converter({
    omitExtraWLInCodeBlocks: true, 
    simplifiedAutoLink: true,
    excludeTrailingPunctuationFromURLs: true,
    literalMidWordUnderscores: true,
    simpleLineBreaks: true
  });

  // Convert the prompt to HTML
  prompt = fixCodeBlocks(prompt);
  console.log("Prompt in setPrompt: ", prompt)
  var html = converter.makeHtml(`**You:** ${prompt}`);
  document.getElementById("prompt-text").innerHTML = html;
}

  // Listen for keyup events on the prompt input element
  document.getElementById('prompt-input').addEventListener('keyup', function (e) {
    // If the key that was pressed was the Enter key
    if (e.keyCode === 13) {
      vscode.postMessage({
        type: 'prompt',
        value: this.value
      });
    }
  });
})();
