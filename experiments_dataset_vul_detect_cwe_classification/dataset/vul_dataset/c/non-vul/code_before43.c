// From cwe-snippets, snippets_90/non-compliant/C/cwe-0252/char_sscanf_01.c

static void func()
{
    {
        char dataBuffer[100] = "";
        char * data = dataBuffer;
        if (sscanf(SRC, "%99s\0", data) == EOF)
        {
            printLine("sscanf failed!");
        }
    }
}