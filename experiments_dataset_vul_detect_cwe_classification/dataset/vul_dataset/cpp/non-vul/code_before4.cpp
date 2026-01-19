// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0191/int_fgets_multiply_33.cpp

static void func()
{
    int data;
    int &dataRef = data;
    /* Initialize data */
    data = 0;
    {
        char inputBuffer[CHAR_ARRAY_SIZE] = "";
        if (fgets(inputBuffer, CHAR_ARRAY_SIZE, stdin) != NULL)
        {
            /* Convert to int */
            data = atoi(inputBuffer);
        }
        else
        {
            printLine("fgets() failed.");
        }
    }
    {
        int data = dataRef;
        if(data < 0) /* ensure we won't have an overflow */
        {
            if (data > (INT_MIN/2))
            {
                int result = data * 2;
                printIntLine(result);
            }
            else
            {
                printLine("data value is too small to perform multiplication.");
            }
        }
    }
}