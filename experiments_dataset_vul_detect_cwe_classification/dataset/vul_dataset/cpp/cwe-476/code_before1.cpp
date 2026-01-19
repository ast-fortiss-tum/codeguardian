// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0476/char_33.cpp

void func()
{
    char * data;
    char * &dataRef = data;
    data = NULL;
    {
        char * data = dataRef;
        printHexCharLine(data[0]);
    }
}