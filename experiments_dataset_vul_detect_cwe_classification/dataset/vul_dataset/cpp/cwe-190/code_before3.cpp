// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0190/unsigned_int_rand_add_73b.cpp

void func(list<unsigned int> dataList)
{
    /* copy data out of dataList */
    unsigned int data = dataList.back();
    {
        unsigned int result = data + 1;
        printUnsignedLine(result);
    }
}