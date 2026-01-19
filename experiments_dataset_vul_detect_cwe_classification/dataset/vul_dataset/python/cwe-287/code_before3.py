# From cwe-snippets, snippets_3/non-compliant/Python/0135.py

import requests

requests.request('GET', 'https://example.domain', verify=False) # Noncompliant
requests.get('https://example.domain', verify=False) # Noncompliant