// Source: Row 2 in ./dataset/CVEfixes/Analysis/results/Java/df_java_cwe_78.xlsx

public void testEscapeSingleQuotesOnArgument()
{
    Shell sh = newShell();

    sh.setWorkingDirectory( "/usr/bin" );
    sh.setExecutable( "chmod" );

    String[] args = { "arg'withquote" };

    List shellCommandLine = sh.getShellCommandLine( args );

    String cli = StringUtils.join( shellCommandLine.iterator(), " " );
    System.out.println( cli );
    assertEquals("cd '/usr/bin' && 'chmod' 'arg'\"'\"'withquote'", shellCommandLine.get(shellCommandLine.size() - 1));
}