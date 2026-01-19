// From cwe-snippets, snippets_90/non-compliant/C/cwe-0253/wchar_t_fputs_18.c

static void func()
{
    goto sink;
sink:
    if (fputws(L"string", stdout) == WEOF)
    {
        printLine("fputws failed!");
    }
}
}