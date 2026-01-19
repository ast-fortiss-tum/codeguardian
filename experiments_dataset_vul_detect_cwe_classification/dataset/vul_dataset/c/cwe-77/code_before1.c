// From cwe-snippets, ./snippets_1/non-compliant/C/0003.c

int main(int argc, char** argv) {
    char cmd[CMD_MAX] = "/usr/bin/cat ";
                      strcat(cmd, argv[1]);
                      system(cmd);
}