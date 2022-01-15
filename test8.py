from uuid import uuid4

# 3. Rename the `environ` to env object for more concise code


from requests import session
from requests_oauthlib import OAuth1Session
import os
import glob
import requests
from requests_oauthlib import OAuth2, OAuth2Session
from urllib.parse import parse_qs, urlencode, unquote
from urllib.request import urlopen, Request
import pandas as pd
import numpy as np
import base64
import hashlib

import os
import re

import requests





def open_connection():
    print("Accessing Ety's Web Server......")
    print("--------------------------------")

    client_key = 'yb9gwm6403ugxhgfmlknav41'
    client_secret = '7awvsg99o0'

    scope = urlencode({'scope':'address_r address_w billing_r cart_r cart_w email_r favorites_r favorites_w feedback_r listings_d listings_r listings_w profile_r profile_w recommend_r recommend_w shops_r shops_w transactions_r transactions_w'})
    HEADER = {"x-api-key": 'yb9gwm6403ugxhgfmlknav41'}
    # "address_r": "see billing and shipping addresses",
    # "address_w": "update billing and shipping addresses",
    # "billing_r": "see all billing statement data",
    # "cart_r": "read shopping carts",
    # "cart_w": "add/remove from shopping carts",
    # "email_r": "Read a member's email address",
    # "favorites_r": "see private favorites",
    # "favorites_w": "add/remove favorites",
    # "feedback_r": "see purchase info in feedback",
    # "listings_d": "delete listings",
    # "listings_r": "see all listings (including expired etc)",
    # "listings_w": "create/edit listings",
    # "profile_r": "see all profile data",
    # "profile_w": "update user profile, avatar, etc",
    # "recommend_r": "see recommended listings",
    # "recommend_w": "accept/reject recommended listings",
    # "shops_r": "see private shop info",
    # "shops_w": "update shop",
    # "transactions_r": "see all checkout/payment data",
    # "transactions_w": "update receipts"



    request_token_url = "https://www.etsy.com/oauth/connect"
    access_token_url = "https://openapi.etsy.com/v3/public/oauth/token"


    redirect_uri = 'https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/'
    state = uuid4().hex


    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8')
    code_verifier = re.sub('[^a-zA-Z0-9]+', '', code_verifier)
    code_verifier, len(code_verifier)
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8')
    code_challenge = code_challenge.replace('=', '')
    code_challenge, len(code_challenge)

    params = urlencode({
                 "response_type": 'code',
                 "client_id": client_key,
                 "scope": scope,
                 "redirect_uri": redirect_uri,
                 "state": state,
                 "code_challenge": code_challenge,
                 "code_challenge_method": 'S256',
                 'header': HEADER,
             })

    r = requests.get(url=request_token_url, params=params)
    # session['code_verifier'] = code_verifier
    # session.modified = True
    print(r.content)
    # return '<html><a href=%s>Connect with Etsy</a></html>' % request_token_url


    credentials = parse_qs(r.content)
    resource_owner_key = credentials.get(b'oauth_token')[0].decode()
    resource_owner_secret = credentials.get(b'oauth_token_secret')[0].decode()



    auth_url = unquote(r.content.decode())

    print('Click to this URL for allow access:')
    print(' ')
    print(unquote(r.content.decode()))
    print(' ')
    verifier = input('Paste confirm code:')

    etsy = OAuth1Session(client_key, client_secret=client_secret,
        resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret)

    acc_token = etsy.fetch_access_token(access_token_url, verifier=verifier)
    print(acc_token)
    return etsy

etsy = open_connection()
#
# def get_dataframes(etsy=open_connection()):
#     api_url = 'https://openapi.etsy.com/v2/'
#     shop_id = '6921272'
#     dates = 'limit=150'
#     transaction = etsy.get(api_url + 'shops/' + shop_id + '/transactions'+'?' + dates)
#     transaction_df = pd.DataFrame(transaction.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
#     receipt = etsy.get(api_url + 'shops/' + shop_id + '/receipts'+'?' + dates)
#     receipt_df = pd.DataFrame(receipt.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
#     receipt_dataframe = receipt_df.to_csv('receipt.csv')
#     transaction_dataframe = transaction_df.to_csv('transaction.csv')
#     return receipt_df, transaction_df
#
# print(get_dataframes())
#
#
#
#
