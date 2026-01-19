// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0190/byte_console_readLine_add_01.java

/* goodB2G() - use badsource and goodsink */
private void goodB2G() throws Throwable
{
    byte data;

    /* init data */
    data = -1;

    /* POTENTIAL FLAW: Read data from console with readLine*/
    BufferedReader readerBuffered = null;
    InputStreamReader readerInputStream = null;
    try
    {
        readerInputStream = new InputStreamReader(System.in, "UTF-8");
        readerBuffered = new BufferedReader(readerInputStream);
        String stringNumber = readerBuffered.readLine();
        if (stringNumber != null)
        {
            data = Byte.parseByte(stringNumber.trim());
        }
    }
    catch (IOException exceptIO)
    {
        IO.logger.log(Level.WARNING, "Error with stream reading", exceptIO);
    }
    catch (NumberFormatException exceptNumberFormat)
    {
        IO.logger.log(Level.WARNING, "Error with number parsing", exceptNumberFormat);
    }
    finally
    {
        /* clean up stream reading objects */
        try
        {
            if (readerBuffered != null)
            {
                readerBuffered.close();
            }
        }
        catch (IOException exceptIO)
        {
            IO.logger.log(Level.WARNING, "Error closing BufferedReader", exceptIO);
        }
        finally
        {
            try
            {
                if (readerInputStream != null)
                {
                    readerInputStream.close();
                }
            }
            catch (IOException exceptIO)
            {
                IO.logger.log(Level.WARNING, "Error closing InputStreamReader", exceptIO);
            }
        }
    }

    /* FIX: Add a check to prevent an overflow from occurring */
    if (data < Byte.MAX_VALUE)
    {
        byte result = (byte)(data + 1);
        IO.writeLine("result: " + result);
    }
    else
    {
        IO.writeLine("data value is too large to perform addition.");
    }

}