// Source: Row 70 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_918.xlsx

String[] urls = request.getParameterValues("fetch");

    if (urls != null)
    {
        HashSet<String> completed = new HashSet<String>();

        for (int i = 0; i < urls.length; i++)
        {
            try
            {
                // Checks if URL already fetched to avoid duplicates
                if (!completed.contains(urls[i]) && Utils.sanitizeUrl(urls[i]))
                {
                    completed.add(urls[i]);
                    URL url = new URL(urls[i]);
                    URLConnection connection = url.openConnection();
                    ByteArrayOutputStream stream = new ByteArrayOutputStream();
                    Utils.copy(connection.getInputStream(), stream);
                    setCachedUrls += "GraphViewer.cachedUrls['"
                            + StringEscapeUtils.escapeEcmaScript(urls[i])
                            + "'] = decodeURIComponent('"
                            + StringEscapeUtils.escapeEcmaScript(
                                    Utils.encodeURIComponent(
                                            stream.toString("UTF-8"),
                                            Utils.CHARSET_FOR_URL_ENCODING))
                            + "');";
                }
            }
            catch (Exception e)
            {
                // ignore
            }
        }
    }