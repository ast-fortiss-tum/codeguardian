// From cwe-snippets, snippets_2/non-compliant/JavaScript/0030.js

var options = {
    key : fs.readFileSync('my-server-key.pem'),
    cert : fs.readFileSync('server-cert.pem'),
    requestCert: true,
  }
  https.createServer(options);