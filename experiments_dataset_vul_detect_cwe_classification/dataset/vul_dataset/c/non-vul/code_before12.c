// From cwe-snippets, snippets_90/non-compliant/C/cwe-0190/char_fscanf_multiply_17.c

static void func()
{
    int h,j;
    char data;
    data = ' ';
    for(h = 0; h < 1; h++)
    {
        data = 2;
    }
    for(j = 0; j < 1; j++)
    {
        if(data > 0) /* ensure we won't have an underflow */
        {
            char result = data * 2;
            printHexCharLine(result);
        }
    }
}