// From cwe-snippets, snippets_2/non-compliant/C/0055.c

ctx.getAuthUserName(?userName); {
CString query = "SELECT * FROM items WHERE owner = '"
     + userName + "' AND itemname = '"
     + request.Lookup("item") + "'";
dbms.ExecuteSQL(query);
