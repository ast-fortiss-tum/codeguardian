// From cwe-snippets, snippets_90/non-compliant/C/cwe-0457/struct_16.c

static void func()
{
    twoIntsStruct data;
    while(1)
    {
        data.intOne = 1;
        data.intTwo = 2;
        break;
    }
    while(1)
    {
        printIntLine(data.intOne);
        printIntLine(data.intTwo);
        break;
    }
}