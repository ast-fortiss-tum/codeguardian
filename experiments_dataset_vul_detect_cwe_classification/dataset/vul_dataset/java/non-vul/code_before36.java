// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0209/printStackTrace_01.java

private void good1() throws Throwable
{

    try
    {
        throw new UnsupportedOperationException();
    }
    catch (UnsupportedOperationException exceptUnsupportedOperation)
    {
        IO.writeLine("There was an unsupported operation error"); /* FIX: print a generic message */
    }

}