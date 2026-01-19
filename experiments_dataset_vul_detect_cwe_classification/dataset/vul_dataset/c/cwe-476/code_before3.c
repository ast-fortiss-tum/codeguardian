// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/struct_18.c

void func()
{
    twoIntsStruct * data;
    goto source;
source:
    data = NULL;
    goto sink;
sink:
    printIntLine(data->intOne);
}