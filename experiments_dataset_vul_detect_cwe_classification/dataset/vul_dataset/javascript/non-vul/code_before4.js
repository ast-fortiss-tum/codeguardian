// From JSVulnerabilityDataSet, row no. 9.

websocket: function(error){
    if(util.isError(error)){
      return String(error.message);
    }else{
      return error;
    }
  }