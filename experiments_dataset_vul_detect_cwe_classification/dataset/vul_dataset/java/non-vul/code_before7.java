// Fron cwe-snippets, ./snippets_1/compliant/Java/0176.java

public void checkValid(boolean isValid) {
    if (isValid) {
        System.out.println("Performing processing");
                           doSomethingImportant();
    }
                      else {
        System.out.println("Not Valid, do not perform processing");
                           return;
    }
}