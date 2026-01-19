// From cwe-snippets, snippets_2/non-compliant/JavaScript/0008.js

var cp = require('child_process');
var home = process.env('APPHOME');
var cmd = home + INITCMD;
child = cp.exec(cmd, function(error, stdout, stderr){
});