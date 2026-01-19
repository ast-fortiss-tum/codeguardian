// From cwe-snippets, ./snippets_1/non-compliant/C/0093.c      

seteuid(0);
/* do some stuff */
seteuid(getuid());