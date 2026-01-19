// From cwe-snippets, snippets_2/non-compliant/C/0005.c 

char *lccopy(const char *str) {
char buf[BUFSIZE];
char *p;
strcpy(buf, str);
for (p = buf; *p; p++) {
  if (isupper(*p)) {
   *p = tolower(*p);
  }
}
return strdup(buf);
}