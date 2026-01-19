# Source: Row 159 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_79.xlsx

def format_errormsg(message: str) -> str:
    """Match account names in error messages and insert HTML links for them."""
    match = re.search(ACCOUNT_RE, message)
    if not match:
        return message
    account = match.group()
    url = flask.url_for("account", name=account)
    return (
        message.replace(account, f'<a href="{url}">{account}</a>')
        .replace("for '", "for ")
        .replace("': ", ": ")
    )