# From cwe-snippets, snippets_2/non-compliant/Python/0045.py

def store(request):
    id = request.GET['id']
    result = get_page_from_somewhere()
    response = HttpResponse(result)
    cache_time = 1800
    cache.set("req-" % id, response, cache_time)
    return response