# From cwe-snippets, ./snippets_1/non-compliant/Python/0001.py

def makeNewUserDir(username):
    if invalidUsername(username):
        #avoidCWE-22andCWE-78
        print('Usernames cannot contain invalid characters')
        return False
    try:
        raisePrivileges()
        os.mkdir('/home/' + username)
        lowerPrivileges()
    except OSError:
        print('Unable to create new user directory for user:' + username)
            return False
    
    return True