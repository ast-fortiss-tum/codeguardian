// Source: Row 16 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_918.xlsx

function middleware (req, res) {
    let u = url.parse(req.url, true)


    let headers = {}
    for (let h of allowHeaders) {
      if (req.headers[h]) {
        headers[h] = req.headers[h]
      }
    }

    // GitHub uses user-agent sniffing for git/* and changes its behavior which is frustrating
    if (!headers['user-agent'] || !headers['user-agent'].startsWith('git/')) {
      headers['user-agent'] = 'git/@isomorphic-git/cors-proxy'
    }

    let p = u.path
    let parts = p.match(/\/([^\/]*)\/(.*)/)
    let pathdomain = parts[1]
    let remainingpath = parts[2]
    let protocol = insecure_origins.includes(pathdomain) ? 'http' : 'https'

    fetch(
      `${protocol}://${pathdomain}/${remainingpath}`,
      {
        method: req.method,
        redirect: 'manual',
        headers,
        body: (req.method !== 'GET' && req.method !== 'HEAD') ? req : undefined
      }
    ).then(f => {
      if (f.headers.has('location')) {
        // Modify the location so the client continues to use the proxy
        let newUrl = f.headers.get('location').replace(/^https?:\//, '')
        f.headers.set('location', newUrl)
      }
      res.statusCode = f.status
      for (let h of exposeHeaders) {
        if (h === 'content-length') continue
        if (f.headers.has(h)) {
          res.setHeader(h, f.headers.get(h))
        }
      }
      if (f.redirected) {
        res.setHeader('x-redirected-url', f.url)
      }
      f.body.pipe(res)
    })