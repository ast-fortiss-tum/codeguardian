// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0190/short_rand_square_74b.java

public void func(HashMap<Integer,Short> dataHashMap ) throws Throwable
{
    short data = dataHashMap.get(2);

    short result = (short)(data * data);

    IO.writeLine("result: " + result);

}
