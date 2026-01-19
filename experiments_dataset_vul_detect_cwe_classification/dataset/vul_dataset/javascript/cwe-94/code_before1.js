// Source: Row 2 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_94.xlsx

module.exports = function (src, file) {
    if (typeof src !== 'string') src = String(src);
    
    try {
        Function(src);
        return;
    }
    catch (err) {
        if (err.constructor.name !== 'SyntaxError') throw err;
        return errorInfo(src, file);
    }
};