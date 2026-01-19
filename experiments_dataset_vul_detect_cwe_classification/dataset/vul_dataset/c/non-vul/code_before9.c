// From cwe-snippets, snippets_90/non-compliant/C/cwe-0476/binary_if_16.c

static void good1()
{
    while(1)
    {
        {
            twoIntsStruct *twoIntsStructPointer = NULL;
            /* FIX: Use && in the if statement so that if the left side of the expression fails then
             * the right side will not be evaluated */
            if ((twoIntsStructPointer != NULL) && (twoIntsStructPointer->intOne == 5))
            {
                printLine("intOne == 5");
            }
        }
        break;
    }
}