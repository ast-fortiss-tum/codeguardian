// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0835/for_01.java

private void func() 
{
    for (int i = 0; i >= 0; i = (i + 1) % 256)
    {
        if (i == 10) 
        { 
            break; 
        }
        IO.writeLine(i);
    }
}