// From JSVulnerabilityDataSet, row no. 578 .

function ensureSafeFunction(obj, fullExpression) {
    if (obj) {
      if (obj.constructor === obj) {
        throw $parseMinErr('isecfn',
          'Referencing Function in Angular expressions is disallowed! Expression: {0}',
          fullExpression);
      } else if (obj === CALL || obj === APPLY || obj === BIND) {
        throw $parseMinErr('isecff',
          'Referencing call, apply or bind in Angular expressions is disallowed! Expression: {0}',
          fullExpression);
      }
    }
}  