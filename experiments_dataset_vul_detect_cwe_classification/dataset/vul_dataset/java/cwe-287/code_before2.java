// From cwe-snippets, snippets_2/non-compliant/Java/0135.java

SSLSocketFactory sf = new CustomSSLSocketFactory(trustStore);
sf.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);