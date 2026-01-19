// From JSVulnerabilityDataSet, row no. 4374 .

download(ccUrl, ccTempFile, function(error, bytes) {
    if (error) {
        console.log("  ✖ Download failed: "+error+"\n");
        fail();
    }
    console.log("  ✔ Download complete: "+ccTempFile+" ("+parseInt(bytes/mb, 10)+" mb)\n");
    setTimeout(function() {
        console.log("  Unpacking "+ccTempFile+" ...");
        unpack(ccTempFile, function(error) {
            if (error) {
                console.log("  ✖ Unpack failed: "+error+"\n");
                fail();
            }
            setTimeout(function() { // Let the entry callbacks finish
                console.log("  ✔ Unpack complete.\n");
                configure_jre();
            }, 1000);
        }, function(entry) {
            console.log("  | "+entry["path"]);
        });
    }, 1000);
},