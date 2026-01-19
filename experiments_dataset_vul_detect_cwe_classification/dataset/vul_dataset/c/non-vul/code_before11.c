// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/binary_if_03.c

static void func()
{
    if(5==5)
    {
        {
            twoIntsStruct *twoIntsStructPointer = NULL;
            if ((twoIntsStructPointer != NULL) && (twoIntsStructPointer->intOne == 5))
            {
                printLine("intOne == 5");
            }
        }
    }
}