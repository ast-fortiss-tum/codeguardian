// Source: Row 55 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_20.xlsx

URI.parseUserinfo = function(string, parts) {
    // extract username:password
    var firstBackSlash = string.indexOf('\\');
    var firstSlash = string.indexOf('/');
    var slash = firstBackSlash === -1 ? firstSlash : (firstSlash !== -1 ? Math.min(firstBackSlash, firstSlash): firstSlash)
    var pos = string.lastIndexOf('@', firstSlash > -1 ? firstSlash : string.length - 1);
    var t;

    // authority@ must come before /path or \path
    if (pos > -1 && (slash === -1 || pos < slash)) {
      t = string.substring(0, pos).split(':');
      parts.username = t[0] ? URI.decode(t[0]) : null;
      t.shift();
      parts.password = t[0] ? URI.decode(t.join(':')) : null;
      string = string.substring(pos + 1);
    } else {
      parts.username = null;
      parts.password = null;
    }

    return string;
  };