// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0126/new_char_memcpy_22a.cpp

void func()
{
    char * data;
    data = NULL;
    badGlobal = 1; /* true */
    data = badSource(data);
    {
        char dest[100];
        memset(dest, 'C', 100-1);
        dest[100-1] = '\0'; /* null terminate */
        memcpy(dest, data, strlen(dest)*sizeof(char));
        dest[100-1] = '\0';
        printLine(dest);
        delete [] data;
    }
    ;
}