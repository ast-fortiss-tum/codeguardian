// From cwe-snippets, snippets_2/non-compliant/C/0048.c

if (!access(file,W_OK)) {
    f = fopen(file,"w+");
    operate(f);
  }
  else {
    fprintf(stderr,"Unable to open file %s.\n",file);
  }