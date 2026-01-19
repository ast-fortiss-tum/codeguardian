// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0511/rand_01.java

private void good1() throws Throwable
{
    if ((new SecureRandom()).nextInt() == 20000)
    {
        IO.writeLine("Sorry, your license has expired.  Please contact support.");
    }
}