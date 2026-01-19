// From cwe-snippets, snippets_2/non-compliant/C++/0040.cpp

int main(int argc, char** argv) {
  char* ret = memchr(argv[0], 'x', MAX_PATH);
  printf("%s\n", ret);
}