// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0546/BUG_07.java 

private void func() throws Throwable
{
    if (privateFive != 5)
    {
        IO.writeLine("Benign, fixed string");
    }
    else
    {
        IO.writeLine("This a test of the emergency broadcast system");
    }
}