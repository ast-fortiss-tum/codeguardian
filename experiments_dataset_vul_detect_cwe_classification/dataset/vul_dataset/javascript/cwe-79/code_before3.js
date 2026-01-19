// From cwe-snippets, snippets_2/non-compliant/JavaScript/0017.js

let element = JSON.parse(getUntrustedInput());
ReactDOM.render(<App>
    {element}
</App>);