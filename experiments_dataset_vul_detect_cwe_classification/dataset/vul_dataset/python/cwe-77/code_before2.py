# From cwe-snippets, snippets_2/non-compliant/Python/0002.py

home = os.getenv('APPHOME')
cmd = home.join(INITCMD)
os.system(cmd);