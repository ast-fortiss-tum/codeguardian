// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0758/char_new_use_05.cpp 

static void func()
{
    if(staticTrue)
    {
        {
            char data;
            data = 5;
            char * pointer = new char;
            *pointer = data; 
            {
                char data = *pointer;
                printHexCharLine(data);
            }
            delete pointer;
        }
    }
}