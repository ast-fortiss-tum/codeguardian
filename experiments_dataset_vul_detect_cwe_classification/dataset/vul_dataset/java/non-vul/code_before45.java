// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0395/basic_02.java

private void func() throws Throwable
{
    if (false)
    {
        IO.writeLine("Benign, fixed string");
    }
    else
    {

        String systemProperty = System.getProperty("CWE395");

        if (systemProperty != null) 
        {
            if (systemProperty.equals("CWE395"))
            {
                IO.writeLine("systemProperty is CWE395");
            }
        }
        else
        {
            IO.writeLine("systemProperty is null");
        }

    }
}