// From cwe-snippets, snippets_90/non-compliant/C/cwe-0401/char_calloc_01.c

static void func()
{
    char * data;
    data = NULL;
    data = (char *)calloc(100, sizeof(char));
    if (data == NULL) {exit(-1);}
    /* Initialize and make use of data */
    strcpy(data, "A String");
    printLine(data);
    free(data);
}
