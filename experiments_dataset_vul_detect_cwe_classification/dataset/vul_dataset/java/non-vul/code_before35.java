// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0193/do_02.java

void func() throws Throwable
{
    if (true)
    {
        int[] intArray = new int[10];
        int i = 0;
        do
        {
            IO.writeLine("intArray[" + i + "] = " + (intArray[i] = i));
            i++;
        }
        while (i < intArray.length);   
    }
}