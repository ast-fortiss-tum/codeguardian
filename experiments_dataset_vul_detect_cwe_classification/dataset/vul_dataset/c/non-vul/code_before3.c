// From cwe-snippets, ./snippets_1/compliant/C/0143.c

foo=malloc(sizeof(char)); //the next line checks to see if malloc failed
                 if (foo==NULL) {
    printf("Malloc failed to allocate memory resources");
                      return -1;
}