from urllib.parse import urlencode

import constants
import requests

access_token = constants.Bearer_Token
# api_call_headers = {'Authorization': 'Bearer ' + access_token}
headers = {
           'x-api-key': constants.api_key,
           'Authorization': 'Bearer ' + access_token
           }

params = {'state': 'active'}
response = requests.get('https://openapi.etsy.com/v3/application/listings', params=params, headers=headers)
# response = requests.get('https://openapi.etsy.com/v3/application/listings/active?', params=params, headers=headers)
print(response.json())
print(response.headers)
print(response.url)













