// From JSVulnerabilityDataSet, row no. 4467 .

function forceWrite() {
    Object.keys(Buffer).forEach(function(name) {
        if (Buffer[name]) {
            jqconsole.Write(Buffer[name], name);
            Buffer[name] = '';
        }
    });
}

function log(data) {
    write(data, 'log-msg');
}

function error(data) {
    write(data, 'error-msg');
}