// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0015/connect_tcp_03.java

private void func() throws Throwable
    {
        String data;
        if (5 == 5)
        {
            data = "foo";
        }
        else
        {
            data = null;
        }

        Connection dbConnection = null;

        try
        {
            dbConnection = IO.getDBConnection();
            dbConnection.setCatalog(data);
        }
        catch (SQLException exceptSql)
        {
            IO.logger.log(Level.WARNING, "Error getting database connection", exceptSql);
        }
        finally
        {
            try
            {
                if (dbConnection != null)
                {
                    dbConnection.close();
                }
            }
            catch (SQLException exceptSql)
            {
                IO.logger.log(Level.WARNING, "Error closing Connection", exceptSql);
            }
        }

    }