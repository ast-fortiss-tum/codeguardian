// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0459/temp_file_01.java

private void func() throws Throwable
{

    File tempFile = null;

    try
    {
        tempFile = File.createTempFile("temp", "1234");
        IO.writeLine(tempFile.toString());

        /* FIX: Call deleteOnExit() so that the file will be deleted */
        tempFile.deleteOnExit();

        /* Set the permissions to avoid insecure temporary file incidentals  */
        if (!tempFile.setWritable(true, true))
        {
            IO.logger.log(Level.WARNING, "Could not set Writable permissions");
        }
        if (!tempFile.setReadable(true, true))
        {
            IO.logger.log(Level.WARNING, "Could not set Readable permissions");
        }
        if (!tempFile.setExecutable(false))
        {
            IO.logger.log(Level.WARNING, "Could not set Executable permissions");
        }
    }
    catch (IOException exceptIO)
    {
        IO.logger.log(Level.WARNING, "Could not create temporary file", exceptIO);
    }

}