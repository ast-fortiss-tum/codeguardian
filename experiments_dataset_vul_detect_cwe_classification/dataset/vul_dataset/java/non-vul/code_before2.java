// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0114/basic_10.java

private void func() throws Throwable
{
    if (IO.staticTrue)
    {
        String root;
        String libraryName = "test.dll";
        if(System.getProperty("os.name").toLowerCase().indexOf("win") >= 0)
        {
            /* running on Windows */
            root = "C:\\libs\\";
        }
        else
        {
            /* running on non-Windows */
            root = "/home/user/libs/";
        }
        System.load(root + libraryName);
    }
}
