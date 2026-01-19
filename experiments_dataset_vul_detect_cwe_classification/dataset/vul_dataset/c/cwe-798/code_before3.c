// From cwe-snippets, snippets_2/non-compliant/C/0042.c

char *stored_password = "";
readPassword(stored_password);
if(safe_strcmp(stored_password, user_password))
    // Access protected resources
}