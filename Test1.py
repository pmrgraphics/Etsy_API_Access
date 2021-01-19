
from requests_oauthlib import OAuth1Session
import constants
import pandas as pd


api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


api_url = constants.api_url
shop_id = constants.shop_id
listing_id = 197564673

req_url = (api_url + 'listings/' + '%s')%listing_id     # thie equates to  'https://openapi.etsy.com/v2/listings/197564673' at runtime

# req_url = 'https://openapi.etsy.com/v2/listings/%s'%(listing_id)


listing_data = { 'listing_id': int(listing_id),
                 'tags': ['Sixpence Coin Cufflinks', 'coin jewelry', 'Golden Wedding Anniversary', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1961', 'gift from 1961', '60th birthday for him', '60th for dad', '60th gift for dad', 'gift for men'],
                 'materials': ['1961 lucky Sixpence', 'cufflinks', 'french cufflink backs', 'Gold Plated cuff links', '1961 Lucky Sixpence Coins']
               }

print(etsy.get(req_url).json())   # returns expected json detail for record listing_id

# TODO Problem code snippit to fix
print(etsy.put(req_url, data=listing_data))   # returns <Response [403]>

# This API works and returns json data for transactions and receipt data
dates = 'limit=150'
transaction = etsy.get(api_url + 'shops/' + shop_id + '/transactions'+'?' + dates)
transaction_df = pd.DataFrame(transaction.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
receipt = etsy.get(api_url + 'shops/' + shop_id + '/receipts'+'?' + dates)
receipt_df = pd.DataFrame(receipt.json()['results']).sort_values(by=['receipt_id'], ascending=False).reset_index(drop=True)
receipt_dataframe = receipt_df.to_csv('receipt.csv')
transaction_dataframe = transaction_df.to_csv('transaction.csv')
print(receipt_df)
print(transaction_df)