// From cwe-snippets, snippets_2/non-compliant/C++/0013.cpp

int main(char* argc, char** argv) {
char cmd[CMD_MAX] = "/usr/bin/cat ";
strcat(cmd, argv[1]);
system(cmd);
}