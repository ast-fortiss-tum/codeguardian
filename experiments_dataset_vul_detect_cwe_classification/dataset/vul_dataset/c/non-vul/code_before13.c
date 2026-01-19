// Fro cwe-snippets, snippets_90/non-compliant/C/cwe-0476/deref_after_check_01.c

static void func()
{
    {
        int *intPointer = NULL;
        if (intPointer == NULL)
        {
            printLine("pointer is NULL");
        }
    }
}