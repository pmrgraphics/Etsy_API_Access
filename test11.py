


from urllib.parse import urlencode
from uuid import uuid4
import base64
import hashlib
import os
import re
from flask import Flask, request, session
import requests
from base64 import b64encode
from os import urandom
import constants

app = Flask(__name__)

# scope = urlencode({'scope': 'listings_d listings_r listings_w transactions_r transactions_w'})
scope = ({'scope': 'listings_d listings_r listings_w transactions_r transactions_w'})

API_BASE = 'https://www.etsy.com/'
# API_BASE = 'https://openapi.etsy.com/v3/public'
API_BASE_TOKEN = 'https://openapi.etsy.com/v3/public'
CLIENT_ID = constants.api_key
CLIENT_SECRET = constants.shared_secret
REDIRECT_URI = 'https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/'
HEADER = {"x-api-key": CLIENT_ID}


code = 'u5fwiegob8bdvk4crujoqbdjjx_dhmya9v9snonpfafczqnri22deuneogle8w2uevpjpkf7hvw3e-p56gylhrpxwkf9yascg3ln'
response = requests.post('https://openapi.etsy.com/v3/public/oauth/token', data={
                                                                        'grant_type': 'authorization_code',
                                                                        'code': code,
                                                                        'client_id': CLIENT_ID,
                                                                        'client_secret': CLIENT_SECRET,
                                                                        'code_verifier': 'k0a6YAqjgWo2n6pOwzdqlBVoMcAU6a3rUFO5b3hSh0Mh2G7i4Rg',
                                                                        'redirect_uri': REDIRECT_URI,})
print(response.json())