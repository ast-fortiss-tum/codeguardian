// From cwe-snippets, ./snippets_1/compliant/JavaScript/0003.js

var newWindow = window.open("http://site.example.com/upage.html", "_blank");
newWindow.opener = null;