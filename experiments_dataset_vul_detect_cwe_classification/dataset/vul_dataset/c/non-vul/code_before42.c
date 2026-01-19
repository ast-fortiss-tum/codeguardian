// From cwe-snippets, snippets_90/non-compliant/C/cwe-0252/char_fputc_13.c

static void func()
{
    if(GLOBAL_CONST_FIVE==5)
    {
        if (fputc((int)'A', stdout) == EOF)
        {
            printLine("fputc failed!");
        }
    }
}
