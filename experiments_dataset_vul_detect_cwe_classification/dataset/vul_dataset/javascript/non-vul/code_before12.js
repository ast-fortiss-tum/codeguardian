// From JSVulnerabilityDataSet, row no.488-490.

peek: function(i) {
    var num = i || 1;
    return (this.index + num < this.text.length) ? this.text.charAt(this.index + num) : false;
  },

  isNumber: function(ch) {
    return ('0' <= ch && ch <= '9');
  },

  isWhitespace: function(ch) {
    // IE treats non-breaking space as \u00A0
    return (ch === ' ' || ch === '\r' || ch === '\t' ||
            ch === '\n' || ch === '\v' || ch === '\u00A0');
  },

  isIdent: function(ch) {
    return ('a' <= ch && ch <= 'z' ||
            'A' <= ch && ch <= 'Z' ||
            '_' === ch || ch === '$');
  },