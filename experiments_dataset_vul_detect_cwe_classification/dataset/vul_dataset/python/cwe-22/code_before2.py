# From cwe-snippets, snippets_2/non-compliant/Python/0050.py

rName = req.field('reportName')
rFile = os.open("/usr/local/apfr/reports/" + rName)
os.unlink(rFile);