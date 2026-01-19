// From cwe-snippets, snippets_2/non-compliant/Java/0277.java

productCategory = this.getIntent().getExtras().getString("productCategory");
sortColumn = this.getIntent().getExtras().getString("sortColumn");
customerID = getAuthenticatedCustomerID(customerName, customerCredentials);
c = invoicesDB.query(Uri.parse(invoices), columns, "productCategory = '" + productCategory + "' and customerID = '" + customerID + "'", null, null, null, "'" + sortColumn + "'asc", null);