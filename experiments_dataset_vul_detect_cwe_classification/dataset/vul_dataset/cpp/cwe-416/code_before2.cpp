// From cwe-snippets, snippets_90/non-compliant/C++/cwe-0416/malloc_free_char_43.cpp 

data = (char *)malloc(100*sizeof(char));
if (data == NULL) {exit(-1);}
memset(data, 'A', 100-1);
data[100-1] = '\0';
/* POTENTIAL FLAW: Free data in the source - the bad sink attempts to use data */
free(data);