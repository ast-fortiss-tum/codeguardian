// From cwe-snippets, snippets_90/non-compliant/C/cwe-0015/w32_01.c

static void func()
{
    char * data;
    char dataBuffer[100] = "";
    data = dataBuffer;
    strcpy(data, "hostname");
    if (!SetComputerNameA(data))
    {
        printLine("Failure setting computer name");
        exit(1);
    }
}