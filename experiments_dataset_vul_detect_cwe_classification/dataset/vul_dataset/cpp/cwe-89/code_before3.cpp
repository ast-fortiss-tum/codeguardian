// From cwe-snippets, snippets_2/non-compliant/C++/0057.cpp

sprintf (sql, "SELECT * FROM items WHERE owner='%s' AND itemname='%s'", username, request.Lookup("item"));
printf("SQL to execute is: \n\t\t %s\n", sql);
rc = sqlite3_exec(db,sql, NULL,0, ?err);