// Source: Row 4 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_78.xlsx

function main(){
    //Try using pkg-config, but if it fails and it is on Windows, try the fallback
    exec("pkg-config " + opencv + " " + flag, function(error, stdout, stderr){
        if(error){
            if(process.platform === "win32"){
                fallback();
            }
            else{
                throw new Error("ERROR: failed to run: pkg-config", opencv, flag);
            }
        }
        else{
            console.log(stdout);
        }
    });
}