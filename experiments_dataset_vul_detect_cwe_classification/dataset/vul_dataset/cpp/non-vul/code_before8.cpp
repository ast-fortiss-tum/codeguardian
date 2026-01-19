// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0758/wchar_t_pointer_new_use_01.cpp

static void func()
{
    {
        wchar_t * data;
        data = L"string";
        wchar_t * * pointer = new wchar_t *;
        *pointer = data; 
        {
            wchar_t * data = *pointer;
            printWLine(data);
        }
        delete pointer;
    }
}