// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0511/time_13.java

private void func() throws Throwable
{
    if (IO.STATIC_FINAL_FIVE == 5)
    {
        Calendar calendarNow = Calendar.getInstance();
        Calendar calendarCheck = Calendar.getInstance();
        calendarCheck.set(2020, 1, 1);
        if (calendarNow.after(calendarCheck))
        {
            IO.writeLine("Sorry, your license has expired.  Please contact support.");
        }
    }
}