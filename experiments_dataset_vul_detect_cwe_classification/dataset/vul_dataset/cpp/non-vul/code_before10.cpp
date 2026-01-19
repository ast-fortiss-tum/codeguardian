// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0464/basic_33.cpp

static void func()
{
    char data;
    char &dataRef = data;
    data = ' ';
    data = 'a';
    {
        char data = dataRef;
        {
            char charArraySink[4];
            charArraySink[0] = 'x';
            charArraySink[1] = data;
            charArraySink[2] = 'z';
            charArraySink[3] = '\0';
            printLine(charArraySink);
        }
    }
}