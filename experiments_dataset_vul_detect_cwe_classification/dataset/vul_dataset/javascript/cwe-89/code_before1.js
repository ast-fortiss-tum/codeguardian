// from cwe-snippets, snippets_2/non-compliant/JavaScript/0054.js

var username = document.form.username.value;
var itemName = document.form.itemName.value;
var query = "SELECT * FROM items WHERE owner = " + username + " AND itemname = " + itemName + ";";
db.transaction(function (tx) {
  tx.executeSql(query);
  }
)