// From cwe-snippets, snippets_2/non-compliant/Java/0073.java

@Path("/myResource")
@Produces("application/json")
public class SomeResource {
@GET
public String doGetAsJson(@QueryParam("param") String param) {
        return "{'name': '" + param + "'}";
}
}