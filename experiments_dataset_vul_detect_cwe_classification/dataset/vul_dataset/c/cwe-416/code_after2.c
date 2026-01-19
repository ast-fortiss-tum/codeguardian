// From cwe-snippets, snippets_90/non-compliant/C/cwe-0416/malloc_free_char_02.c

static void goodG2B2()
{
    char * data;
    /* Initialize data */
    data = NULL;
    if(1)
    {
        data = (char *)malloc(100*sizeof(char));
        if (data == NULL) {exit(-1);}
        memset(data, 'A', 100-1);
        data[100-1] = '\0';
        /* FIX: Do not free data in the source */
    }
    if(1)
    {
        /* POTENTIAL FLAW: Use of data that may have been freed */
        printLine(data);
        /* POTENTIAL INCIDENTAL - Possible memory leak here if data was not freed */
    }
}