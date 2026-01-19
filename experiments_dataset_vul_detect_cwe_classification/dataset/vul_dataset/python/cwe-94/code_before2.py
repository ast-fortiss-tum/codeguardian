# From cwe-snippets, snippets_2/non-compliant/Python/0056.py

from django.http import HttpResponse
from jinja2 import Template as Jinja2_Template
from jinja2 import Environment, DictLoader, escape
def process_request(request):
    # Load the template
    template = request.GET['template']
    t = Jinja2_Template(template)
    name = source(request.GET['name'])
    # Render the template with the context data
    html = t.render(name=escape(name))
    return HttpResponse(html)