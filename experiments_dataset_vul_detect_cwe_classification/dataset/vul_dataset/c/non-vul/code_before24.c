// From cwe-snippets, snippets_90/non-compliant/C/cwe-0758/char_alloca_use_02.c

static void func()
{
    if(1)
    {
        {
            char data;
            char * pointer = (char *)ALLOCA(sizeof(char));
            data = 5;
            *pointer = data; 
            {
                char data = *pointer;
                printHexCharLine(data);
            }
        }
    }
}