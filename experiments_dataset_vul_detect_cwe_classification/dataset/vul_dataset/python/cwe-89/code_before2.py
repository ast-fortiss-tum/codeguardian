# From cwe-snippets, snippets_2/non-compliant/Python/0046.py

userName = req.field('userName')
emailId = req.field('emaiId')
results = db.emails.find({"$where", "this.owner == \"" + userName + "\" ?? this.emailId == \"" + emailId + "\""});