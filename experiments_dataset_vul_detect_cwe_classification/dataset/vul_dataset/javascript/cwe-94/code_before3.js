// From cwe-snippets, snippets_2/non-compliant/JavaScript/0050.js

app.get('/', function(req, res){
    var template = _.template(req.params['template']);
    res.write("<html><body><h2>Hello World!</h2>" + template() + "</body></html>");
});