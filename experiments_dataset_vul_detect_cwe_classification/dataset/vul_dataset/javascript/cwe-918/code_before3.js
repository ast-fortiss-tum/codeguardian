// Source: Row 171 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_918.xlsx

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
      const origin = url.origin != null
        ? url.origin
        : `${url.protocol}//${url.hostname}:${port}`
      const path = url.path != null
        ? url.path
        : `${url.pathname || ''}${url.search || ''}`
  
      url = new URL(path, origin)
    }
  
    return url
  }