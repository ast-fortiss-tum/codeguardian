// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/long_04.c

static void func()
{
    long * data;
    long tmpData = 5L;
    if(STATIC_CONST_TRUE)
    {
        /* FIX: Initialize data */
        {
            data = &tmpData;
        }
    }
    if(STATIC_CONST_TRUE)
    {
        printLongLine(*data);
    }
}