// From cwe-snippets, snippets_2/non-compliant/C++/0004.cpp

char buf[64], in[MAX_SIZE];
printf("Enter buffer contents:\n");
read(0, in, MAX_SIZE-1);
printf("Bytes to copy:\n");
scanf("%d", ?bytes);
memcpy(buf, in, bytes);