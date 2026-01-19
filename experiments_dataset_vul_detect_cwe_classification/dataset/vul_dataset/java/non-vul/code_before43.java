// From cwe-snippets, snippets_90/non-compliant/Java/cwe-0382/Servlet_Runtime_01.java

private void func(HttpServletRequest request, HttpServletResponse response) throws Throwable
{
    response.getWriter().write("You cannot shut down this application, only the admin can");

}