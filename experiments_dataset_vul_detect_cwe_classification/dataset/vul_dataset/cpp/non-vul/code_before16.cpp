// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0762/delete_array_char_malloc_01.cpp

static void func()
{
    char * data;
    /* Initialize data*/
    data = NULL;
    data = (char *)malloc(100*sizeof(char));
    if (data == NULL) {exit(-1);}
    free(data);
}

