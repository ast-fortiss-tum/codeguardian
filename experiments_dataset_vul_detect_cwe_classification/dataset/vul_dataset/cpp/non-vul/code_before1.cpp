// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0190/char_fscanf_add_73b.cpp

void func(list<char> dataList)
{
    char data = dataList.back();
    if (data < CHAR_MAX)
    {
        char result = data + 1;
        printHexCharLine(result);
    }
    else
    {
        printLine("data value is too large to perform arithmetic safely.");
    }
}