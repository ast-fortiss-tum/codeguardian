// From cwe-snippets, snippets_2/non-compliant/JavaScript/0006.js

function MyController(function($stateParams, $interpolate){
    var ctx = { foo : 'bar' };
    var interpolated = $interpolate($stateParams.expression);
    this.rendered = interpolated(ctx);
}