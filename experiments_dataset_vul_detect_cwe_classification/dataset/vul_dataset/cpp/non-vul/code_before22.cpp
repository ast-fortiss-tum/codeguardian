// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0563/unused_uninit_variable_long_33.cpp

static void func()
{
    long data;
    long &dataRef = data;
    {
        long data = dataRef;
        data = 5L;
        printLongLine(data);
    }
}