// From cwe-snippets, 

static void helper(void *args)
{
    int *pIntArgs = (int *)args;
    int i;
    stdThreadLockAcquire(gGoodLock);
    for (i = 0; i < N_ITERS; i++)
    {
        *pIntArgs = *pIntArgs + 1;
    }
    stdThreadLockRelease(gGoodLock);
}