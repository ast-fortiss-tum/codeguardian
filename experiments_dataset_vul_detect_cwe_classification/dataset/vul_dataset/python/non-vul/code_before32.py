# Source: Row 48 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def logout(request):
    """ Clears the session and logs the current user out. """
    request.user_logout()
    # FIXME(gabriel): we don't ship a view named splash
    return shortcuts.redirect('splash')