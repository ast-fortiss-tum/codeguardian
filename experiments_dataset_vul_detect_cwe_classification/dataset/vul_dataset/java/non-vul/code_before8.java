// From cwe-snippets, ./snippets_1/compliant/Java/0177.java

public void checkValid(boolean isValid) {
    if (!isValid) {
        System.out.println("Not Valid, do not perform processing");
                           return;
    }
                      System.out.println("Performing processing");
                      doSomethingImportant();
}