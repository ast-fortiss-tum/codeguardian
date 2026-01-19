// From cwe-snippets, snippets_90/non-compliant/C/cwe-0563/unused_value_wchar_t_05.c

static void func()
{
    wchar_t data;
    if(staticTrue)
    {
        data = L'W';
        printf("%02lx\n", data);
    }
    if(staticTrue)
    {
        data = L'Z';
        printf("%02lx\n", data);
    }
}