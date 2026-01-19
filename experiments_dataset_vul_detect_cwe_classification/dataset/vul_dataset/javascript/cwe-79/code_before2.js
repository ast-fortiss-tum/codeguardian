// From cwe-snippets, snippets_2/non-compliant/JavaScript/0015.js

<SCRIPT>
var pos=document.URL.indexOf("eid=")+4;
document.write(document.URL.substring(pos,document.URL.length));
</SCRIPT>