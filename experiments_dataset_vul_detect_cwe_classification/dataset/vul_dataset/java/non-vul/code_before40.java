// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0325/MessageDigest_update_01.java

private void func() throws Throwable
{

    final String HASH_INPUT = "ABCDEFG123456";

    MessageDigest messageDigest = MessageDigest.getInstance("SHA-512");

    /* FIX: Include call to MessageDigest.update() */
    messageDigest.update(HASH_INPUT.getBytes("UTF-8"));

    IO.writeLine(IO.toHex(messageDigest.digest()));

}