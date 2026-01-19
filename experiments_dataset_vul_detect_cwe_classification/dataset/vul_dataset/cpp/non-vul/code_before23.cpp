// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0758/int_new_use_01.cpp

static void func()
{
    {
        int data;
        data = 5;
        int * pointer = new int;
        *pointer = data; 
        {
            int data = *pointer;
            printIntLine(data);
        }
        delete pointer;
    }
}