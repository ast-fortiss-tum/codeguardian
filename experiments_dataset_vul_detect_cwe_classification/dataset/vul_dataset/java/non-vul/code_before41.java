// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0329/basic_01.java

private void func() throws Throwable
{

    byte[] text = "asdf".getBytes("UTF-8");

    KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
    keyGenerator.init(128);
    SecretKey key = keyGenerator.generateKey();

    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");

    int blockSize = cipher.getBlockSize();
    byte[] initializationVector = new byte[blockSize];
    SecureRandom secureRandom = new SecureRandom();
    secureRandom.nextBytes(initializationVector);
    IvParameterSpec ivParameterSpec = new IvParameterSpec(initializationVector);

    cipher.init(Cipher.ENCRYPT_MODE, key, ivParameterSpec);

    IO.writeLine(IO.toHex(cipher.doFinal(text)));

}
