// Source: Row 5 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_22.xlsx

var url2FilePath = function(url){
    var subPath = url.substr("/tests/frontend".length);
    if (subPath == ""){
      subPath = "index.html"
    }
    subPath = subPath.split("?")[0];

    var filePath = path.normalize(path.join(rootTestFolder, subPath));
    // make sure we jail the paths to the test folder, otherwise serve index
    if (filePath.indexOf(rootTestFolder) !== 0) {
      filePath = path.normalize(path.join(rootTestFolder, "index.html"));
    }
    return filePath;
  }