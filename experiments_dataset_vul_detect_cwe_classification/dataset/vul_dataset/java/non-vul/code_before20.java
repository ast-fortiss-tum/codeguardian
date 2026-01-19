// From cwe-snippets, ./snippets_1/compliant/Java/0208.java

private final void readObject(ObjectInputStream in) throws java.io.IOException {
                 throw new java.io.IOException("Cannot be deserialized"); }