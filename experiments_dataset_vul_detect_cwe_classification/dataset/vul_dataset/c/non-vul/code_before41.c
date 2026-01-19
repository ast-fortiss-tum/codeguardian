// From cwe-snippets, snippets_90/non-compliant/C/cwe-0252/char_fgets_01.c

static void func()
{
    {
        char dataBuffer[100] = "";
        char * data = dataBuffer;
        printLine("Please enter a string: ");
        if (fgets(data, 100, stdin) == NULL)
        {
            printLine("fgets failed!");
            exit(1);
        }
        printLine(data);
    }
}