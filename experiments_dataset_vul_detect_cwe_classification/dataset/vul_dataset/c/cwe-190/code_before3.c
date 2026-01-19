// From cwe-snippets, snippets_90/non-compliant/C/cwe-0190/char_fscanf_square_31.c

void func()
{
    char data;
    data = ' ';
    fscanf (stdin, "%c", &data);
    {
        char dataCopy = data;
        char data = dataCopy;
        {
            char result = data * data;
            printHexCharLine(result);
        }
    }
}