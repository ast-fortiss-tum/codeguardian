// From JSVulnerabilityDataSet, row no. 52.

server.sendMessage = function(connection, message){
    let stringResponse = '';
    if(connection.rawConnection.method !== 'HEAD'){
      stringResponse = String(message);
    }

    cleanHeaders(connection);
    const headers = connection.rawConnection.responseHeaders;
    const responseHttpCode = parseInt(connection.rawConnection.responseHttpCode);

    server.sendWithCompression(connection, responseHttpCode, headers, stringResponse);
  };