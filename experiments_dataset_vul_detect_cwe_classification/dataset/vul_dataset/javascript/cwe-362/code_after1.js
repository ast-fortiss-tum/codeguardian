database_connect.query('SELECT * FROM users WHERE name == ? AND password = ? LIMIT 1', userNameFromUser, passwordFromUser, function(err, results){
    var authenticated = false;
    if (!err && results.length > 0){
      authenticated = true;
    }
    if (authenticated){
      //do something privileged stuff
      authenticatedActions();
    }else{
      sendUnathenticatedMessage();
    }
  });
  