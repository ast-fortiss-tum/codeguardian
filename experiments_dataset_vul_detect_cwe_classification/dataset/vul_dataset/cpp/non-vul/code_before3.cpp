// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0369/float_fgets_73a.cpp

static void func()
{
    float data;
    list<float> dataList;
    /* Initialize data */
    data = 0.0F;
    data = 2.0F;
    dataList.push_back(data);
    dataList.push_back(data);
    dataList.push_back(data);
    goodG2BSink(dataList);
}