// From cwe-snippets, snippets_2/non-compliant/Java/0138.java

private void WriteToFile(String what_to_write) {
    try{
        File root = Environment.getExternalStorageDirectory();
        if(root.canWrite()) {
            File dir = new File(root + "write_to_the_SDcard");
            File datafile = new File(dir, number + ".extension");
            FileWriter datawriter = new FileWriter(datafile);
            BufferedWriter out = new BufferedWriter(datawriter);
            out.write(what_to_write);
            out.close();
            }
    }
}