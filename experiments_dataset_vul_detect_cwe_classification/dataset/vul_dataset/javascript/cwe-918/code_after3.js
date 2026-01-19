// Source: Row 172 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_918.xlsx

function parseURL (url) {
    if (typeof url === 'string') {
      url = new URL(url)
    }
  
    if (!url || typeof url !== 'object') {
      throw new InvalidArgumentError('invalid url')
    }
  
    if (url.port != null && url.port !== '' && !Number.isFinite(parseInt(url.port))) {
      throw new InvalidArgumentError('invalid port')
    }
  
    if (url.path != null && typeof url.path !== 'string') {
      throw new InvalidArgumentError('invalid path')
    }
  
    if (url.pathname != null && typeof url.pathname !== 'string') {
      throw new InvalidArgumentError('invalid pathname')
    }
  
    if (url.hostname != null && typeof url.hostname !== 'string') {
      throw new InvalidArgumentError('invalid hostname')
    }
  
    if (url.origin != null && typeof url.origin !== 'string') {
      throw new InvalidArgumentError('invalid origin')
    }
  
    if (!/^https?:/.test(url.origin || url.protocol)) {
      throw new InvalidArgumentError('invalid protocol')
    }
  
    if (!(url instanceof URL)) {
      const port = url.port != null
        ? url.port
        : (url.protocol === 'https:' ? 443 : 80)
      let origin = url.origin != null
        ? url.origin
        : `${url.protocol}//${url.hostname}:${port}`
      let path = url.path != null
        ? url.path
        : `${url.pathname || ''}${url.search || ''}`
  
      if (origin.endsWith('/')) {
        origin = origin.substring(0, origin.length - 1)
      }
  
      if (path && !path.startsWith('/')) {
        path = `/${path}`
      }
      // new URL(path, origin) is unsafe when `path` contains an absolute URL
      // From https://developer.mozilla.org/en-US/docs/Web/API/URL/URL:
      // If first parameter is a relative URL, second param is required, and will be used as the base URL.
      // If first parameter is an absolute URL, a given second param will be ignored.
      url = new URL(origin + path)
    }
  
    return url
  }