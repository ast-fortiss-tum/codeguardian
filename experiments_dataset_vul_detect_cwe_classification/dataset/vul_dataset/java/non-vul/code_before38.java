// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0252/FileInputStream_01.java

private void func() throws Throwable
{

    FileInputStream streamFileInput = null;

    try
    {
        int bytesToRead = 1024;
        byte[] byteArray = new byte[bytesToRead];

        streamFileInput = new FileInputStream("c:\\file.txt");

        int numberOfBytesRead = streamFileInput.read(byteArray);

        if (numberOfBytesRead == -1)
        {
            IO.writeLine("The end of the file has been reached.");
        }
        else
        {
            if (numberOfBytesRead < bytesToRead)
            {
                IO.writeLine("Could not read " + bytesToRead + " bytes.");
            }
            else
            {
                IO.writeLine(new String(byteArray, "UTF-8"));
            }
        }
    }
    catch (FileNotFoundException exceptFileNotFound)
    {
        IO.logger.log(Level.WARNING, "FileNotFoundException opening file", exceptFileNotFound);
    }
    catch(IOException exceptIO)
    {
        IO.logger.log(Level.WARNING, "IOException reading file", exceptIO);
    }
    finally
    {
        try
        {
            if(streamFileInput != null)
            {
                streamFileInput.close();
            }
        }
        catch(IOException exceptIO)
        {
            IO.logger.log(Level.WARNING, "IOException closing FileInputStream", exceptIO);
        }
    }

}