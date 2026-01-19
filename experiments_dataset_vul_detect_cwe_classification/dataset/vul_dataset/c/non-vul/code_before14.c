// From cwe-snippets, snippets_90/non-compliant/C/cwe-0124/CWE839_fgets_01.c

static void func()
{
    int data;
    /* Initialize data */
    data = 7;
    {
        int i;
        int buffer[10] = { 0 };
        if (data < 10)
        {
            buffer[data] = 1;
            /* Print the array values */
            for(i = 0; i < 10; i++)
            {
                printIntLine(buffer[i]);
            }
        }
        else
        {
            printLine("ERROR: Array index is negative.");
        }
    }
}