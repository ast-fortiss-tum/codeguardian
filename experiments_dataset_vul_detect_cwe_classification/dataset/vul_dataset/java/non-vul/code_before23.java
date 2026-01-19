// From cwe-snippets, ./snippets_1/compliant/Java/0330.java

long count = 0L;
for (long i = 0; i < Integer.MAX_VALUE; i++) {
    count += i;
}