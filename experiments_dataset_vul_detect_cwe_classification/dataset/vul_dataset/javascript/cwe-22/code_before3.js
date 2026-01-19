// Source: Row 37 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_22.xlsx


Project.prototype.getFile = function (filePath,treeish) {
  if (treeish !== "_") {
      return gitTools.getFile(this.path, filePath, treeish);
  } else {
      let fullPath = fspath.join(this.path,filePath);
      if (/^\.\./.test(fspath.relative(this.path,fullPath))) {
          throw new Error("Invalid file name")
      }
      return fs.readFile(fspath.join(this.path,filePath),"utf8");
  }
};