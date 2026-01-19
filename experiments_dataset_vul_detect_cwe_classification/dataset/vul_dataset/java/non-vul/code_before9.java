// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0078/connect_tcp_41.java

private void func1(String data ) throws Throwable
{

    String osCommand;
    if(System.getProperty("os.name").toLowerCase().indexOf("win") >= 0)
    {
        /* running on Windows */
        osCommand = "c:\\WINDOWS\\SYSTEM32\\cmd.exe /c dir ";
    }
    else
    {
        /* running on non-Windows */
        osCommand = "/bin/ls ";
    }

    Process process = Runtime.getRuntime().exec(osCommand + data);
    process.waitFor();

}

private void func2() throws Throwable
{
    String data;

    /* FIX: Use a hardcoded string */
    data = "foo";

    func1(data  );
}