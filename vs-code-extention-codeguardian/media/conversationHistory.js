// conversationHistory.js content

document.addEventListener('DOMContentLoaded', function() {
    // Ensure the DOM is fully loaded before trying to access elements
    var responseElement = document.getElementById('response');
    if (responseElement) {
        // Insert a static string into the 'response' element
        responseElement.innerHTML = '<p>Static string loaded successfully from conversationHistory.js</p>';
    } else {
        console.error('Element with ID "response" not found.');
    }
});
