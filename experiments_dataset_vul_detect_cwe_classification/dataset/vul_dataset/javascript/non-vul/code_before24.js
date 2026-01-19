// From JSVulnerabilityDataSet, row no. 4974 .

xdescribe('navigator.webkitGetUserMedia', function () {
    it('calls its callbacks', function (done) {
      navigator.webkitGetUserMedia({
        audio: true,
        video: false
      }, function () {
        done()
      }, function () {
        done()
      })
    })
  })