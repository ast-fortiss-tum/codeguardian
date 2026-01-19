// From cwe-snippets, snippets_2/non-compliant/Java/0181.java

String user = request.getParameter("user");
SMTPSSLTransport transport = new SMTPSSLTransport(session,new URLName(Utilities.getProperty("smtp.server")));
transport.connect(Utilities.getProperty("smtp.server"), username, password);
transport.simpleCommand("VRFY " + user);