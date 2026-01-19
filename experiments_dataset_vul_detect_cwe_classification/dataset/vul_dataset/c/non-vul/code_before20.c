// From cwe-snippets, snippets_90/non-compliant/C/cwe-0457/struct_array_alloca_no_init_18.c

static void goodG2B()
{
    twoIntsStruct * data;
    data = (twoIntsStruct *)ALLOCA(10*sizeof(twoIntsStruct));
    goto source;
source:
    {
        int i;
        for(i=0; i<10; i++)
        {
            data[i].intOne = i;
            data[i].intTwo = i;
        }
    }
    goto sink;
sink:
    {
        int i;
        for(i=0; i<10; i++)
        {
            printIntLine(data[i].intOne);
            printIntLine(data[i].intTwo);
        }
    }
}