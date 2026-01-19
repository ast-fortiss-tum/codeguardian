// From JSVulnerabilityDataSet, row 6380

(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
    typeof define === 'function' && define.amd ? define(factory) :
    (global.Qty = factory());
  }(this, function () { 'use strict';
  
    /**
     * Tests if a value is a Qty instance
     *
     * @param {*} value - Value to test
     *
     * @returns {boolean} true if value is a Qty instance, false otherwise
     */
    function isQty(value) {
      return value instanceof Qty;
    }
