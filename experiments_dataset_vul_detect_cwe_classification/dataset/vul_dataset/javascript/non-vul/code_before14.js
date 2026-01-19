// From JSVulnerabilityDataSet, row no. 696 .

function JQLite(element) {
    if (element instanceof JQLite) {
      return element;
    }
  
    var argIsString;
  
    if (isString(element)) {
      element = trim(element);
      argIsString = true;
    }
    if (!(this instanceof JQLite)) {
      if (argIsString && element.charAt(0) != '<') {
        throw jqLiteMinErr('nosel', 'Looking up elements via selectors is not supported by jqLite! See: http://docs.angularjs.org/api/angular.element');
      }
      return new JQLite(element);
    }
  
    if (argIsString) {
      jqLiteAddNodes(this, jqLiteParseHTML(element));
    } else {
      jqLiteAddNodes(this, element);
    }
  }