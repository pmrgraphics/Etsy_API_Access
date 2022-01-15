from requests_oauthlib import OAuth1Session
import os
import glob
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs, urlencode, unquote
from urllib.request import urlopen, Request
import pandas as pd
import numpy as np



def open_connection():
    print("Accessing Ety's Web Server......")
    print("--------------------------------")

    client_key = 'yb9gwm6403ugxhgfmlknav41'
    client_secret = '7awvsg99o0'

    scope = urlencode({'scope':'listings_w transactions_r'})
    request_token_url = f"https://openapi.etsy.com/v2/oauth/request_token?{scope}"
    access_token_url = 'https://openapi.etsy.com/v2/oauth/access_token'

    oauth = OAuth1(client_key, client_secret=client_secret)
    r = requests.post(url=request_token_url, auth=oauth)
    r.content
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

# etsy = open_connection()

def get_dataframes(etsy=open_connection()):
    api_url = 'https://openapi.etsy.com/v2/'
    shop_id = '6921272'
    dates = 'limit=150'
    transaction = etsy.get(api_url + 'shops/' + shop_id + '/transactions'+'?' + dates)
    transaction_df = pd.DataFrame(transaction.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
    receipt = etsy.get(api_url + 'shops/' + shop_id + '/receipts'+'?' + dates)
    receipt_df = pd.DataFrame(receipt.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
    receipt_dataframe = receipt_df.to_csv('receipt.csv')
    transaction_dataframe = transaction_df.to_csv('transaction.csv')
    return receipt_df, transaction_df

print(get_dataframes())

# def put_data(etsy=open_connection()):
#     listing_id = '197564673'
#
#     listing_data = {
#             'tags': ['Sixpence Coin Cufflinks', 'coin jewelry', 'Golden Wedding Anniversary', 'antique cufflinks', 'Anniversary Cufflinks',
#                      '1961', 'gift from 1961', '60th birthday for him', '60th for dad', '60th gift for dad', 'gift for men']
#                }
#     api_url = 'https://openapi.etsy.com/v2/'
#     shop_id = '6921272'
#
#     item = etsy.put(api_url + '/listings/' + listing_id + '?')
#
#     return item
# print(put_data)


