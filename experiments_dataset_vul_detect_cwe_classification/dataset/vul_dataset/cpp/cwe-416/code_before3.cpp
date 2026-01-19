// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0416/new_delete_array_class_13.cpp

void func()
{
    TwoIntsClass * data;
    /* Initialize data */
    data = NULL;
    if(GLOBAL_CONST_FIVE==5)
    {
        data = new TwoIntsClass[100];
        {
            size_t i;
            for(i = 0; i < 100; i++)
            {
                data[i].intOne = 1;
                data[i].intTwo = 2;
            }
        }
        delete [] data;
    }
    if(GLOBAL_CONST_FIVE==5)
    {
        printIntLine(data[0].intOne);
    }
}