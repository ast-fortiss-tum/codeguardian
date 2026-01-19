// From cwe-snippets, snippets_2/non-compliant/Java/0290.java   

VelocityContext context = new VelocityContext();
context.put( "name", user.name );
// Load the template
String template = getUserTemplateFromRequestBody(request);
RuntimeServices runtimeServices = RuntimeSingleton.getRuntimeServices();
StringReader reader = new StringReader(template);
SimpleNode node = runtimeServices.parse(reader, "myTemplate");
template = new Template();
template.setRuntimeServices(runtimeServices);
template.setData(node);
template.initDocument();
// Render the template with the context data
StringWriter sw = new StringWriter();
template.merge( context, sw );
