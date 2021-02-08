from time import sleep

from requests_oauthlib import OAuth1Session
import os
import constants

import pandas as pd

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret



df = pd.read_csv('image.csv')

for index, row in df.iterrows():
    listing_id = int(row['listing_id'])
    listing_image_id = int(row['listing_image_id'])

    response = OAuth1Session(client_key=api_key,
                             client_secret=shared_secret,
                             resource_owner_key=oauth_token,
                             resource_owner_secret=oauth_token_secret)


    sleep(0.5)
    uri = 'https://openapi.etsy.com/v2/listings/' + f'{listing_id}' + '/images/' + f'{listing_image_id}'
    params = {'listing_id': f'{listing_id}', 'listing_image_id': f'{listing_image_id}'}
    result = response.delete(uri, params=params)
    print(result.text)














