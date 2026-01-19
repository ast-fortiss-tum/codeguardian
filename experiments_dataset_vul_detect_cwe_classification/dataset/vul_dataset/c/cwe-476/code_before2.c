// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/long_04.c

void func()
{
    long * data;
    if(STATIC_CONST_TRUE)
    {
        data = NULL;
    }
    if(STATIC_CONST_TRUE)
    {
        printLongLine(*data);
    }
}