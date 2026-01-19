// From cwe-snippets, snippets_90/non-compliant/C/cwe-0190/char_fscanf_multiply_01.c

void func()
{
    char data;
    data = ' ';
    fscanf (stdin, "%c", &data);
    if(data > 0) /* ensure we won't have an underflow */
    {
        char result = data * 2;
        printHexCharLine(result);
    }
}