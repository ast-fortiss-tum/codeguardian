// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0672/list_int_01.cpp

static void func()
{
    list<int>  data;
    data.push_back(100);
    data.push_back(0);
    {
        list<int> ::iterator i;
        cout << "The list contains: ";
        for( i = data.begin(); i != data.end(); i++)
        {
            cout << " " << *i;
        }
        cout << endl;
    }
}


