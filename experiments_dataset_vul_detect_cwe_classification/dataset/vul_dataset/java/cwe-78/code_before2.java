// From cwe-snippets, ./snippets_1/non-compliant/Java/0014.java

String script = System.getProperty("SCRIPTNAME");
if (script != null)
System.exec(script);