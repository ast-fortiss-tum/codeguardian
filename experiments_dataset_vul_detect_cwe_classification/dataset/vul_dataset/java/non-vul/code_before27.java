// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0476/Integer_06.java

private void func() throws Throwable
    {
        Integer data;
        if (PRIVATE_STATIC_FINAL_FIVE==5)
        {
            data = null;
        }
        else
        {
            data = null;
        }

        if (PRIVATE_STATIC_FINAL_FIVE==5)
        {
            if (data != null)
            {
                IO.writeLine("" + data.toString());
            }
            else
            {
                IO.writeLine("data is null");
            }
        }
    }

