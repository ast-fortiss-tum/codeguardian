// Source: Row 7 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_77.xlsx

resolve: function resolve(hostname, type) {
    var nodeBinary = process.execPath;

    if (!isValidHostName(hostname)) {
        console.error('Invalid hostname:', hostname);
        return null;
    }
    if (typeof type !== 'undefined' && RRecordTypes.indexOf(type) === -1) {
        console.error('Invalid rrtype:', type);
        return null;
    }

    var scriptPath = path.join(__dirname, "../scripts/dns-lookup-script"),
        response,
        cmd = util.format('"%s" "%s" %s %s', nodeBinary, scriptPath, hostname, type || '');

    response = shell.exec(cmd, {silent: true});
    if (response && response.code === 0) {
        return JSON.parse(response.stdout);
    }
    debug('hostname', "fail to resolve hostname " + hostname);
    return null;
}