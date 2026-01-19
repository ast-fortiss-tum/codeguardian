// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0336/basic_01.java

private void func() throws Throwable
{

    SecureRandom secureRandom = new SecureRandom();

    IO.writeLine("" + secureRandom.nextInt());
    IO.writeLine("" + secureRandom.nextInt());

}