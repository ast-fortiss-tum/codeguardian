// From JSVulnerabilityDataSet, row no. 4481 .

plugin.ext('onPreResponse', function (request, reply) {

    // Add to view context

    var response = request.response;

    if (settings.addToViewContext &&
        request.plugins.crumb &&
        request.route.plugins._crumb &&
        !response.isBoom &&
        response.variety === 'view') {

        response.source.context = response.source.context || {};
        response.source.context[request.route.plugins._crumb.key] = request.plugins.crumb;
    }

    return reply();
});