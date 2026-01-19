# From cwe-snippets, snippets_2/non-compliant/Python/0044.py  

user = request.GET['user']
session = smtplib.SMTP(smtp_server, smtp_tls_port)
session.ehlo()
session.starttls()
session.login(username, password)
session.docmd("VRFY", user)