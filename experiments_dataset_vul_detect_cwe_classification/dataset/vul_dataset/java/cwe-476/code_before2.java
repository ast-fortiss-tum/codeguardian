// From cwe-snippets, snippets_3/non-compliant/Java/0008.java

public MainClass(String color) {
if (color != null) {
    secondary = null;
}
primary = color;  
}