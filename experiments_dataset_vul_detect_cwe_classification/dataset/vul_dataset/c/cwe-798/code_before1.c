// From cwe-snippets, cat ./snippets_1/non-compliant/C/0266.c

int VerifyAdmin(char *password) {
    if (strcmp(password,"68af404b513073584c4b6f22b6c63e6b")) {
                           printf("Incorrect Password!\n");
                           return(0);
    }
                       return(1);
}