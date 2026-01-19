// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0396/dotdotdot_08.cpp

static void func()
{
    if(staticReturnsTrue())
    {
        try
        {
            if (rand()%2 == 0)
            {
                throw out_of_range("err1");
            }
            if (rand()%2 == 0)
            {
                throw domain_error("err2");
            }
        }
        catch (out_of_range &)
        {
            printLine("out_of_range");
        }
        catch (domain_error &)
        {
            printLine("domain_error");
            return;
        }
        printLine("ok");
    }
}