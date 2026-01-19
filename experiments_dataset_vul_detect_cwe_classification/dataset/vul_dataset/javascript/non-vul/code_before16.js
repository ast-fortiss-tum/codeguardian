// From JSVulnerabilityDataSet, row no. 9134 .

decorateTemplateData: function(data) {
    if (this.app) {
      data._app = this.app;
    }
    if (this.model) {
      data._model = this.model;
    }
    if (this.collection) {
      data._collection = this.collection;
    }
    data._view = this;
    return data;
  },