// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0248/Error_01.java

private void func() 
{
    try
    {
        throw new Error("Really bad Error");
    }
    catch(Error error)
    {
        IO.logger.log(Level.WARNING, "Caught an Error", error);
    }
}