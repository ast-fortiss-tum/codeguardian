// From cwe-snippets, snippets_90/non-compliant/C/cwe-0416/malloc_free_long_06.c

static void func()
{
    char * data;
    data = NULL;
    if(STATIC_CONST_FIVE!=5)
    {
        printLine("Benign, fixed string");
    }
    else
    {
        data = (char *)malloc(100*sizeof(char));
        if (data == NULL) {exit(-1);}
        memset(data, 'A', 100-1);
        data[100-1] = '\0';
    }
    if(STATIC_CONST_FIVE==5)
    {
        printLine(data);
    }
}