// From JSVulnerabilityDataSet, row no. 4662 .

describe('remote promise', function () {
  it('can be used as promise in each side', function (done) {
    var promise = remote.require(path.join(fixtures, 'module', 'promise.js'))
    promise.twicePromise(Promise.resolve(1234)).then(function (value) {
      assert.equal(value, 2468)
      done()
    })
  })

  it('handles rejections via catch(onRejected)', function (done) {
    var promise = remote.require(path.join(fixtures, 'module', 'rejected-promise.js'))
    promise.reject(Promise.resolve(1234)).catch(function (error) {
      assert.equal(error.message, 'rejected')
      done()
    })
  })

