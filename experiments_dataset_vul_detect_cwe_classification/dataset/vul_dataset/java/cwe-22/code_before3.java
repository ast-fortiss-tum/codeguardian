// From cwe-snippets, snippets_2/non-compliant/Java/0214.java  

String rName = request.getParameter("reportName");
File rFile = new File("/usr/local/apfr/reports/" + rName);
rFile.delete();