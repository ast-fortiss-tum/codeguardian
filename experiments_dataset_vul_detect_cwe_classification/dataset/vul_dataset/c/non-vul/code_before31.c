// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/struct_18.c

static void func()
{
    twoIntsStruct * data;
    twoIntsStruct tmpData;
    goto source;
source:
    {
        tmpData.intOne = 0;
        tmpData.intTwo = 0;
        data = &tmpData;
    }
    goto sink;
sink:
    printIntLine(data->intOne);
}