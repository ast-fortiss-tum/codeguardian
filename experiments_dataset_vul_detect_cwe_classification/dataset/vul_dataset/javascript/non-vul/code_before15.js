// From JSVulnerabilityDataSet, row no. 2015 .

c3_chart_internal_fn.init = function () {
    var $$ = this, config = $$.config;

    $$.initParams();

    if (config.data_url) {
        $$.convertUrlToData(config.data_url, config.data_mimeType, config.data_headers, config.data_keys, $$.initWithData);
    }
    else if (config.data_json) {
        $$.initWithData($$.convertJsonToData(config.data_json, config.data_keys));
    }
    else if (config.data_rows) {
        $$.initWithData($$.convertRowsToData(config.data_rows));
    }
    else if (config.data_columns) {
        $$.initWithData($$.convertColumnsToData(config.data_columns));
    }
    else {
        throw Error('url or json or rows or columns is required.');
    }
};
