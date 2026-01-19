# Source: Row 5 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_78.xlsx

@component(AuthenticationProvider)
class OSAuthenticationProvider(AuthenticationProvider):
    id = 'os'
    name = 'OS users'
    allows_sudo_elevation = True

    def authenticate(self, username, password):
        child = None

        if PY3:
            from shlex import quote
        else:
            from pipes import quote

        try:
            child = pexpect.spawn('/bin/sh', ['-c', '/bin/su -c "/bin/echo SUCCESS" - %s' % quote(username)], timeout=5)
            child.expect('.*:')
            child.sendline(password)
            result = child.expect(['su: .*', 'SUCCESS'])
        except Exception as err:
            if child and child.isalive():
                child.close()
            logging.error('Error checking password: %s', err)
            return False
        if result == 0:
            return False
        else:
            return True

    def authorize(self, username, permission):
        return True

    def get_isolation_uid(self, username):
        return pwd.getpwnam(username).pw_uid
