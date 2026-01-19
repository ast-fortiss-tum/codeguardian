// From JSVulnerabilityDataSet, row no.122.

forEach(hasDirectives[name], function(directiveFactory) {
    try {
      var directive = $injector.invoke(directiveFactory);
      if (isFunction(directive)) {
        directive = { compile: valueFn(directive) };
      } else if (!directive.compile && directive.link) {
        directive.compile = valueFn(directive.link);
      }
      directive.priority = directive.priority || 0;
      directive.name = directive.name || name;
      directive.require = directive.require || (directive.controller && directive.name);
      directive.restrict = directive.restrict || 'A';
      directives.push(directive);
    } catch (e) {
      $exceptionHandler(e);
    }
  });