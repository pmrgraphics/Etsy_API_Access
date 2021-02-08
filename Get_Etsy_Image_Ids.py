from time import sleep

from requests_oauthlib import OAuth1Session
import os
import constants

import pandas as pd

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret



df = pd.read_csv('test.csv')

for index, row in df.iterrows():
    listing_id = int(row['listing_id'])

    response = OAuth1Session(client_key=api_key,
                             client_secret=shared_secret,
                             resource_owner_key=oauth_token,
                             resource_owner_secret=oauth_token_secret)


    listing_image_id = 1
    uri = 'https://openapi.etsy.com/v2/listings/%s/images' % listing_id
    params = {'listing_id': f'{listing_id}', 'listing_image_id': 2}
    images = response.get(uri)
    # result = response.delete(uri, params=params)
    # print(result)

    Image = images.json()

    listings = Image['results']

    for each in listings:
        if listing_id == each['listing_id']:
            lst=[]
            lst.append(each['listing_image_id'])
            print(listing_id, lst)


    # for key, value in Image:
    #     if key['listing_id'] == listing_id:
    #         print(listing_id, key['listing_image_id'], value)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #














