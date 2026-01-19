// Source: Row 5 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_77.xlsx

resolve: function resolve(hostname) {
    var output,
        nodeBinary = process.execPath,
        scriptPath = path.join(__dirname, "../scripts/dns-lookup-script"),
        response,
        cmd = util.format('"%s" "%s" %s', nodeBinary, scriptPath, hostname);

    response = shell.exec(cmd, {silent: true});
    if (response && response.code === 0) {
        output = response.output;
        if (output && net.isIP(output)) {
            return output;
        }
    }
    debug('hostname', "fail to resolve hostname " + hostname);
    return null;
}