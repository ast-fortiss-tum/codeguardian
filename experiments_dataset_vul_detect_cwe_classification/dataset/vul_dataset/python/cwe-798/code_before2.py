# From cwe-snippets, snippets_2/non-compliant/Python/0040.py

import hmac
mac = hmac.new("secret", plaintext).hexdigest()