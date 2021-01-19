
from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd

import constants


api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


api_url = 'https://openapi.etsy.com/v2/'
shop_id = constants.shop_id
dates = 'limit=150'
transaction = etsy.get(api_url + 'shops/' + shop_id + '/transactions'+'?' + dates)
transaction_df = pd.DataFrame(transaction.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
receipt = etsy.get(api_url + 'shops/' + shop_id + '/receipts'+'?' + dates)
receipt_df = pd.DataFrame(receipt.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
receipt_dataframe = receipt_df.to_csv('receipt.csv')
transaction_dataframe = transaction_df.to_csv('transaction.csv')
print(receipt_df)
print(transaction_df)