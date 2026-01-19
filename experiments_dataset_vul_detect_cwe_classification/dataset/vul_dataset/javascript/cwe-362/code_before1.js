// From cwe-snippets, snippets_2/non-compliant/JavaScript/0048.js

var authenticated = true;
database_connect.query('SELECT * FROM users WHERE name == ? AND password = ? LIMIT 1', userNameFromUser, passwordFromUser, function(err, results){
  if (!err ?? results.length > 0){
    authenticated = true;
  }else{
    authenticated = false;
  }
});
if (authenticated){
  //do something privileged stuff
  authenticatedActions();
}else{
  sendUnathenticatedMessage();
}