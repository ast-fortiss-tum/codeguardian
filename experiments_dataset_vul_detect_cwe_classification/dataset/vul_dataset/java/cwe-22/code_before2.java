// From cwe-snippets, ./snippets_1/non-compliant/Java/0006.java

String path = getInputPath();
                 if (path.startsWith("/safe_dir/"))
                 {
    File f = new File(path);
                      f.delete()
}