# From cwe-snippets, snippets_2/non-compliant/Python/0059.py

userName = req.field('userName')
itemName = req.field('itemName')
query = "SELECT * FROM items WHERE owner = ' " + userName +" ' AND itemname = ' " + itemName +"';"
cursor.execute(query)
result = cursor.fetchall()