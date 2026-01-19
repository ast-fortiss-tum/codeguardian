// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0758/class_new_use_01.cpp

static void func()
{
    {
        TwoIntsClass data;
        data.intOne = 1;
        data.intTwo = 2;
        TwoIntsClass * pointer = new TwoIntsClass;
        *pointer = data; 
        {
            TwoIntsClass data = *pointer;
            printIntLine(data.intOne);
            printIntLine(data.intTwo);
        }
        delete pointer;
    }
}