// From JSVulnerabilityDataSet, row no. 4822 .

describe('window.alert(message, title)', function () {
    it('throws an exception when the arguments cannot be converted to strings', function () {
      assert.throws(function () {
        window.alert({toString: null})
      }, /Cannot convert object to primitive value/)

      assert.throws(function () {
        window.alert('message', {toString: 3})
      }, /Cannot convert object to primitive value/)
    })
  })