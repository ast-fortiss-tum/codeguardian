// From cwe-snippets, snippets_90/non-compliant/C/cwe-0078/char_console_execlp_17.c

void func()
{
    int i;
    char * data;
    char dataBuffer[100] = COMMAND_ARG2;
    data = dataBuffer;
    for(i = 0; i < 1; i++)
    {
        {
            /* Read input from the console */
            size_t dataLen = strlen(data);
            /* if there is room in data, read into it from the console */
            if (100-dataLen > 1)
            {
                if (fgets(data+dataLen, (int)(100-dataLen), stdin) != NULL)
                {
                    /* The next few lines remove the carriage return from the string that is
                     * inserted by fgets() */
                    dataLen = strlen(data);
                    if (dataLen > 0 && data[dataLen-1] == '\n')
                    {
                        data[dataLen-1] = '\0';
                    }
                }
                else
                {
                    printLine("fgets() failed");
                    /* Restore NUL terminator if fgets fails */
                    data[dataLen] = '\0';
                }
            }
        }
    }
    /* execlp - searches for the location of the command among
     * the directories specified by the PATH environment variable */
    EXECLP(COMMAND_INT, COMMAND_INT, COMMAND_ARG1, COMMAND_ARG3, NULL);
}