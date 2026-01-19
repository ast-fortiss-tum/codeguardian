// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0190/short_rand_square_74b.java

public void func(HashMap<Integer,Short> dataHashMap ) throws Throwable
{
    short data = dataHashMap.get(2);

    /* NOTE: Math.abs of the minimum int or long will return that same value, so we must check for it */
    if ((data != Integer.MIN_VALUE) && (data != Long.MIN_VALUE) && (Math.abs(data) <= (long)Math.sqrt(Short.MAX_VALUE)))
    {
        short result = (short)(data * data);
        IO.writeLine("result: " + result);
    }
    else
    {
        IO.writeLine("data value is too large to perform squaring.");
    }

}