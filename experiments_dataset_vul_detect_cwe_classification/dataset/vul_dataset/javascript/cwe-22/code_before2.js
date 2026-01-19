// Source: Row 4 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_22.xlsx

var url2FilePath = function(url){
    var subPath = url.substr("/tests/frontend".length);
    if (subPath == ""){
      subPath = "index.html"
    }
    subPath = subPath.split("?")[0];

    var filePath = path.normalize(npm.root + "/../tests/frontend/")
    filePath += subPath.replace("..", "");
    return filePath;
  }