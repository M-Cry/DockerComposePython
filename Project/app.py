import requests
import os

req = requests.get(os.getenv("SITE_URL"))
assert req.status_code == 200

assert 1 == 2