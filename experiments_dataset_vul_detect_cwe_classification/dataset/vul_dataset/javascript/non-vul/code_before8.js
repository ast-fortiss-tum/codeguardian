// From JSVulnerabilityDataSet, row no.96.

request(options, function(err, res, body) {
    if (err) {
      return callback(err);
    }

    if (res.statusCode >= 300) {
      var status = HTTP_STATUS_CODES[res.statusCode];
      return callback(new Error(
        'Deployment failed: ' + res.statusCode + ' ' + status + ': ' + body
      ));
    }

    callback(null, params);
  });