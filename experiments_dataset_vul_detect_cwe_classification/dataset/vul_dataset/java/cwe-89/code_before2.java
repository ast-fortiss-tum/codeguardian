// From cwe-snippets, snippets_2/non-compliant/Java/0276.java

String customerID = getAuthenticatedCustomerID(customerName, customerCredentials);
AmazonSimpleDBClient sdbc = new AmazonSimpleDBClient(appAWSCredentials);
String query = "select * from invoices where productCategory = '"
            + productCategory + "' and customerID = '"
            + customerID + "' order by '"
            + sortColumn + "' asc";
SelectResult sdbResult = sdbc.select(new SelectRequest(query));