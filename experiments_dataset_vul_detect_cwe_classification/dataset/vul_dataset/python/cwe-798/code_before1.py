# From cwe-snippets, snippets_2/non-compliant/Python/0039.py

from hashlib import pbkdf2_hmac
dk = pbkdf2_hmac('sha256', '', salt, 100000)