// From cwe-snippets, snippets_90/non-compliant/C/cwe-0416/malloc_free_long_06.c

static void goodG2B2()
{
    long * data;
    /* Initialize data */
    data = NULL;
    if(STATIC_CONST_FIVE==5)
    {
        data = (long *)malloc(100*sizeof(long));
        if (data == NULL) {exit(-1);}
        {
            size_t i;
            for(i = 0; i < 100; i++)
            {
                data[i] = 5L;
            }
        }
        /* FIX: Do not free data in the source */
    }
    if(STATIC_CONST_FIVE==5)
    {
        if (data != NULL) {
            printLongLine(data[0]);
        }
    }
}