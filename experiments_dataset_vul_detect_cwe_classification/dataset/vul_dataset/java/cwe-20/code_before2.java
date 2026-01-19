// From cwe-snippets, ./snippets_1/non-compliant/Java/0002.java

public static final double price = 20.00;
int quantity = currentUser.getAttribute("quantity");
double total = price * quantity;
chargeUser(total);