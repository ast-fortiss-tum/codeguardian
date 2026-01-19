// From cwe-snippets, snippets_2/non-compliant/Java/0170.java

private static String hmacKey = "";
byte[] keyBytes = hmacKey.getBytes();
SecretKeySpec key = new SecretKeySpec(keyBytes, "SHA1");
Mac hmac = Mac.getInstance("HmacSHA1");
hmac.init(key);