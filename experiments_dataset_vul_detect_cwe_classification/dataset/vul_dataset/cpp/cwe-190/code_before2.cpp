// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0190/char_max_multiply_74b.cpp

void func(map<int, char> dataMap)
{
    /* copy data out of dataMap */
    char data = dataMap[2];
    if(data > 0) /* ensure we won't have an underflow */
    {
        char result = data * 2;
        printHexCharLine(result);
    }
}