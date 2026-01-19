// From cwe-snippets, snippets_2/non-compliant/JavaScript/0009.js

var cp = require('child_process');
var http = require('http');
var url = require('url');
function listener(request, response){
  var btype = url.parse(request.url, true)['query']['backuptype'];
  if (btype !== undefined){
    cmd = "c:\\util\\rmanDB.bat" + btype;
    cp.exec(cmd, function(error, stdout, stderr){
    });
  }
}
http.createServer(listener).listen(8080);