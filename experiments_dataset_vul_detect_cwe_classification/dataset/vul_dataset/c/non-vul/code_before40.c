// From cwe-snippets, snippets_90/non-compliant/C/cwe-0242/basic_02.c

static void func()
{
    if(1)
    {
        {
            char dest[DEST_SIZE];
            char *result;
            result = fgets(dest, DEST_SIZE, stdin);
            /* Verify return value */
            if (result == NULL)
            {
                /* error condition */
                printLine("Error Condition: alter control flow to indicate action taken");
                exit(1);
            }
            dest[DEST_SIZE-1] = '\0';
            printLine(dest);
        }
    }
}