// Source: Row 15 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_863.xlsx

_size ({ id, token }, done) {
    return this.client
      .get(`https://graph.facebook.com/${id}`)
      .qs({ fields: 'images' })
      .auth(token)
      .request((err, resp, body) => {
        if (err || resp.statusCode !== 200) {
          err = this._error(err, resp)
          logger.error(err, 'provider.facebook.size.error')
          return done(err)
        }

        getURLMeta(this._getMediaUrl(body))
          .then(({ size }) => done(null, size))
          .catch((err2) => {
            logger.error(err2, 'provider.facebook.size.error')
            done(err2)
          })
      })
  }