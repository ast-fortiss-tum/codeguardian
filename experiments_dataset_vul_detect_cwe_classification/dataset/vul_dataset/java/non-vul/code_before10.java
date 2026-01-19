// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0459/Servlet_temp_file_03.java

private void good2(HttpServletRequest request, HttpServletResponse response) throws Throwable
    {
        if (5 == 5)
        {
            File tempFile = null;
            try
            {
                tempFile = File.createTempFile("temp", "1234");
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
            finally
            {
                /* FIX: Delete the temporary file manually */
                if (tempFile.exists())
                {
                    tempFile.delete();
                }
            }
        }
    }