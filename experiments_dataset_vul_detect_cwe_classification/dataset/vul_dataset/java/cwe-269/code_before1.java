// From cwe-snippets, ./snippets_1/non-compliant/Java/0085.java   

AccessController.doPrivileged(new PrivilegedAction() {
    public Object run() {
        // privileged code goes here, for example:
                            System.loadLibrary("awt");
                            return null;
                           // nothing to return
    }