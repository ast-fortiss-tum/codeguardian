// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0476/class_05.cpp

void func()
{
    TwoIntsClass * data;
    if(staticTrue)
    {
        data = NULL;
    }
    if(staticTrue)
    {
        printIntLine(data->intOne);
        delete data;
    }
}