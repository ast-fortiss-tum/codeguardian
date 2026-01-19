// From cwe-snippets, snippets_2/non-compliant/JavaScript/0019.js

var http = require('http');
var url = require('url');
function listener(request, response){
  var eid = url.parse(request.url, true)['query']['eid'];
  if (eid !== undefined){
    response.write('<p>Welcome, ' + eid + '!</p>');
  }
}
http.createServer(listener).listen(8080);