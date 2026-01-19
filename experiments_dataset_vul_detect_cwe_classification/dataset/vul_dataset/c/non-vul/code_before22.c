// From cwe-snippets, snippets_90/non-compliant/C/cwe-0775/fopen_no_close_02.c

static void func()
{
    FILE * data;
    data = NULL;
    data = fopen("BadSource_fopen.txt", "w+");
    if(1)
    {
        if (data != NULL)
        {
            fclose(data);
        }
    }
}