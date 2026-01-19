// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0124/char_alloca_ncpy_33.cpp

static void func()
{
    char * data;
    char * &dataRef = data;
    char * dataBuffer = (char *)ALLOCA(100*sizeof(char));
    memset(dataBuffer, 'A', 100-1);
    dataBuffer[100-1] = '\0';
    data = dataBuffer;
    {
        char * data = dataRef;
        {
            char source[100];
            memset(source, 'C', 100-1); /* fill with 'C's */
            source[100-1] = '\0'; /* null terminate */
            /* POTENTIAL FLAW: Possibly copying data to memory before the destination buffer */
            strncpy(data, source, 100-1);
            /* Ensure the destination buffer is null terminated */
            data[100-1] = '\0';
            printLine(data);
        }
    }
}