// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0511/counter_04.java

private void func() throws Throwable
{
    if (PRIVATE_STATIC_FINAL_FALSE)
    {
        IO.writeLine("Benign, fixed string");
    }
    else
    {

        int count = 0;

        do
        {
            if (count == 20000)
            {
                IO.writeLine("Sorry, your license has expired.  Please contact support.");
            }
            count++;
        }
        while (count < Integer.MAX_VALUE);

    }
}