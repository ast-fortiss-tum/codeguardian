// From cwe-snippets, ./snippets_1/non-compliant/C/0265.c

int VerifyAdmin(char *password) {
    if (strcmp(password, "Mew!")) {
        printf("Incorrect Password!\n");
                           return(0)
    }
                       return(1);
}