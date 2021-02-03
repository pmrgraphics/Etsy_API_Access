





from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd
from requests.exceptions import HTTPError
import constants
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


try:
    api_url = 'https://openapi.etsy.com/v2/'
    listing_id = '185057518'

    images = etsy.get(api_url + 'listings/' + listing_id + '/images')
    print(images.text)
    # transaction_df = pd.DataFrame(transaction.json()['results']).sort_values(by=['receipt_id'],
    #                                                                          ascending=False).reset_index(drop=True)
    #
    # transaction_dataframe = transaction_df.to_csv('transaction.csv')


except HTTPError as http_err:
    logging.error("Exception occurred", exc_info=True)
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    logging.error("Exception occurred", exc_info=True)
    print(f'Other error occurred: {err}')
else:
    print('Done')






