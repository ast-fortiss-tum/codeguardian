// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0325/KeyGenerator_init_02.java

private void func() throws Throwable
{
    if (true)
    {
        final String CIPHER_INPUT = "ABCDEFG123456";
        KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
        keyGenerator.init(256);
        SecretKey secretKey = keyGenerator.generateKey();
        byte[] byteKey = secretKey.getEncoded();
        SecretKeySpec secretKeySpec = new SecretKeySpec(byteKey, "AES");
        Cipher aesCipher = Cipher.getInstance("AES");
        aesCipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
        byte[] encrypted = aesCipher.doFinal(CIPHER_INPUT.getBytes("UTF-8"));
        IO.writeLine(IO.toHex(encrypted));
    }
}