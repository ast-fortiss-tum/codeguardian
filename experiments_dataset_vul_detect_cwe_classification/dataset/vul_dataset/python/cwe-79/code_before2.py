# From cwe-snippets, snippets_2/non-compliant/Python/0016.py

req = self.request()# fetch the request object
        eid = req.field('eid',None) # tainted request message
self.writeln("Employee ID:" + eid)