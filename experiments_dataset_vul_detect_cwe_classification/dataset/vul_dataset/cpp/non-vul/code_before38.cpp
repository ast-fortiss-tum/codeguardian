// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0015/w32_33.cpp

static void goodG2B()
{
    char * data;
    char * &dataRef = data;
    char dataBuffer[100] = "";
    data = dataBuffer;
    /* FIX: get the hostname from a string literal */
    strcpy(data, "hostname");
    {
        char * data = dataRef;
        /* POTENTIAL FLAW: set the hostname to data obtained from a potentially external source */
        if (!SetComputerNameA(data))
        {
            printLine("Failure setting computer name");
            exit(1);
        }
    }
}