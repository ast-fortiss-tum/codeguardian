// From cwe-snippets, ./snippets_1/compliant/Java/0325.java

String sessionID = generateSessionId();
Cookie c = new Cookie("session_id", sessionID);
c.setHttpOnly(true);
response.addCookie(c);