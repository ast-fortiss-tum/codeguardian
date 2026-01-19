# Source: Row 878 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

async def handle_404(request, response):
    if 'json' not in response.headers['Content-Type']:
        if request.path.endswith('/'):
            return web.HTTPFound(request.path.rstrip('/'))
        return web.json_response({
            "status": 404,
            "message": "Page '{}' not found".format(request.path)
        }, status=404)
    return response