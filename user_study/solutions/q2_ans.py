# Correct answer: CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
# Source: Row 159 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_79.xlsx

'''
The function takes a user-supplied message string 
and uses it to construct an HTML link without properly sanitizing the input.
The vulnerability lies in the following line:

message.replace(account, f'<a href="{url}">{account}</a>')

If the account variable contains any malicious HTML or JavaScript code, it will be included in the resulting HTML link. 
This could lead to a cross-site scripting (XSS) vulnerability, where an attacker can inject malicious scripts into the web page.

To mitigate this vulnerability, we should properly escape or sanitize the account variable before including it in the HTML link. 
For example, using the escape() function provided by the Flask framework to ensure that the account variable is properly encoded and does not contain any malicious code.
Then, use the Markup class to mark the string as safe for rendering in the HTML template.

'''

from markupsafe import Markup, escape

def format_errormsg(message: str) -> Markup:
    """Match account names in error messages and insert HTML links for them."""
    match = re.search(ACCOUNT_RE, message)
    if not match:
        return Markup(escape(message))
    account = escape(match.group())
    url = escape(flask.url_for("account", name=account))
    safe_message = escape(message)
    linked_message = safe_message.replace(account, Markup(f'<a href="{url}">{account}</a>'))

    return Markup(linked_message)