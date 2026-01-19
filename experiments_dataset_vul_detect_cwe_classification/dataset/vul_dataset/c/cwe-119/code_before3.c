// From cwe-snippets, ./snippets_5/non-compliant/C/0026.c

#include<stdio.h> 
#include<string.h>
#include <unistd.h>
#define MAXLEN 1024

int main(){
    char *inputbuf;
    char *pathbuf[MAXLEN];
    /*for some file descriptor fd*/
    read(0,inputbuf,MAXLEN); //does not null terminate
    strcpy(pathbuf,inputbuf); //requires null terminated input
    return 0;
}