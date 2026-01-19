// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0484/basic_03.java

private void func() throws Throwable
{
    if (5 != 5)
    {
        IO.writeLine("Benign, fixed string");
    }
    else
    {

        int intRandom = (new SecureRandom()).nextInt(3);
        String stringValue;

        switch (intRandom)
        {
        case 1:
            stringValue = "one";
            break;
        case 2:
            stringValue = "two";
            break; 
        default:
            stringValue = "Default";
            break;
        }

        IO.writeLine(stringValue);

    }
}