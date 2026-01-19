// From JSVulnerabilityDataSet, row no.393.

/**
 * @ngdoc method
 * @name $compile.directive.Attributes#$updateClass
 * @kind function
 *
 * @description
 * Adds and removes the appropriate CSS class values to the element based on the difference
 * between the new and old CSS class values (specified as newClasses and oldClasses).
 *
 * @param {string} newClasses The current CSS className value
 * @param {string} oldClasses The former CSS className value
 */
$updateClass : function(newClasses, oldClasses) {
    var toAdd = tokenDifference(newClasses, oldClasses);
    if (toAdd && toAdd.length) {
      $animate.addClass(this.$$element, toAdd);
    }

    var toRemove = tokenDifference(oldClasses, newClasses);
    if (toRemove && toRemove.length) {
      $animate.removeClass(this.$$element, toRemove);
    }
  },