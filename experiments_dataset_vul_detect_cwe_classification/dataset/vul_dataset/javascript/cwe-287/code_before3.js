// From cwe-snippets, snippets_2/non-compliant/JavaScript/0031.js

var tls = require('tls');
tls.connect({
  host: 'https://www.hackersite.com',
  port: '443',
  rejectUnauthorized: false,
});