// From cwe-snippets, snippets_90/non-compliant/C/cwe-0484/basic_02.c

static void func()
{
    if(1)
    {
        {
            int x = (rand() % 3);
            switch (x)
            {
            case 0:
                printLine("0");
                break;
            case 1:
                printLine("1");
                break;
            case 2:
                printLine("2");
                break;
            default:
                printLine("Invalid Number");
                break;
            }
        }
    }
}