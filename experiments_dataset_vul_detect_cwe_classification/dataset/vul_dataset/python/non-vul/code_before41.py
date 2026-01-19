# Source: Row 339 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def _hkey(key):
    if '\n' in key or '\r' in key or '\0' in key:
        raise ValueError("Header names must not contain control characters: %r" % key)
    return key.title().replace('_', '-')