// Source: Row 6 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_78.xlsx

module.exports = function(image, output, cb) {
    if(/;|&|`|\$|\(|\)|\|\||\||!|>|<|\?|\${/g.test(JSON.stringify(image))) {
      console.log('Input Validation failed, Suspicious Characters found');
    } else {
    var cmd = module.exports.cmd(image, output);
    exec(cmd, {timeout: 30000}, function(e, stdout, stderr) {
      if (e) { return cb(e); }
      if (stderr) { return cb(new Error(stderr)); }
  
      return cb(null, output.versions);
    });
  }
  };