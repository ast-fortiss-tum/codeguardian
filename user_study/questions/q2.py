import re
import flask
from flask import request, render_template

ACCOUNT_RE = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def format_errormsg(message: str) -> str:
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
    
app = flask.Flask(__name__)

@app.route("/")
def index():
    error = request.args.get("error")
    if error:
        error_msg = format_errormsg(error)
        return render_template("index.html", error=error_msg)
    return render_template("index.html")