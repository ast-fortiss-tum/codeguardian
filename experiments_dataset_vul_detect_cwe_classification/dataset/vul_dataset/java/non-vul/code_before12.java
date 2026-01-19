// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0470/connect_tcp_06.java

private void func() throws Throwable
{
    String data;
    if (PRIVATE_STATIC_FINAL_FIVE != 5)
    {
        data = null;
    }
    else
    {

        /* FIX: Use a hardcoded class name */
        data = "Testing.test";

    }

    Class<?> tempClass = Class.forName(data);
    Object tempClassObject = tempClass.newInstance();

    IO.writeLine(tempClassObject.toString()); /* Use tempClassObject in some way */

}