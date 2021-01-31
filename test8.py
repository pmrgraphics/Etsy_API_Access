import requests
from oauthlib.oauth1 import SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER
from requests_oauthlib import OAuth1
import oauth2 as oauth, urllib
import constants
import json
from requests.exceptions import HTTPError

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret


listing_id = 174277415

auth = OAuth1(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret,
                     # signature_type=SIGNATURE_TYPE_AUTH_HEADER,
                     # signature_method=SIGNATURE_HMAC,


              )


url = 'https://openapi.etsy.com/v2/listings/'f'{listing_id}'

headers={'Content-Type':'application/x-www-form-urlencoded'}

tags = ['Coin Cufflinks', 'coin jewelry', '97th Birthday', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1924 Farthing', 'gift from 1924', '97th for dad', '97th gift for dad', 'gift for men']
message = {'listing_id': listing_id, 'tags': tags}


try:
    r = requests.put(url, auth=auth, data=message, headers=headers)

    # details = requests.get('https://openapi.etsy.com/v2/listings/'f'{listing_id}', auth=auth)
    # returns listing details ok
    # details = requests.get('https://openapi.etsy.com/v2/oauth/scopes', auth=auth)
    # returns the following scopes ["email_r","listings_r","listings_w","listings_d","transactions_r","billing_r","feedback_r"]

    # If the response was successful, no Exception will be raised
    r.raise_for_status()


except HTTPError as http_err:
    logging.error("Exception occurred", exc_info=True)
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    logging.error("Exception occurred", exc_info=True)
    print(f'Other error occurred: {err}')
else:
    print(r.text)

print(r.request.body)

