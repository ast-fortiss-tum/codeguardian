// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0190/char_fscanf_multiply_72b.cpp

void func(vector<char> dataVector)
{
    char data = dataVector[2];
    if(data > 0) /* ensure we won't have an underflow */
    {
        if (data < (CHAR_MAX/2))
        {
            char result = data * 2;
            printHexCharLine(result);
        }
        else
        {
            printLine("data value is too large to perform arithmetic safely.");
        }
    }
}