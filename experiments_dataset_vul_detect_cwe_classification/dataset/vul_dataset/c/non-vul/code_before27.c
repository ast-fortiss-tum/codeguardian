// From cwe-snippets, snippets_90/non-compliant/C/cwe-0416/malloc_free_char_02.c

static void func()
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
        free(data);
    }
    if(0)
    {
        printLine("Benign, fixed string");
    }
    else
    {
        /* do nothing */
    }
}