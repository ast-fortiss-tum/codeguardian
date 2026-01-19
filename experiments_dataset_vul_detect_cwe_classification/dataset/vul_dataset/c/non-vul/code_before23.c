// From cwe-snippets, snippets_90/non-compliant/C/cwe-0688/basic_11.c

static void func()
{
    if(globalReturnsTrue())
    {
        {
            char dest[DEST_SIZE];
            int intFive = 5;
            sprintf(dest, "%d", intFive);
            printLine(dest);
        }
    }
}