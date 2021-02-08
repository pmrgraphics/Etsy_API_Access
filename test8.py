from time import sleep

from requests_oauthlib import OAuth1Session
import os
import constants

import pandas as pd
from etsy2 import Etsy

from etsy2.oauth import EtsyOAuthClient
from requests.exceptions import HTTPError

import logging




logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


df = pd.read_csv('test.csv')

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy_oauth = EtsyOAuthClient(client_key=api_key,
                            client_secret=shared_secret,
                            resource_owner_key=oauth_token,
                            resource_owner_secret=oauth_token_secret)

etsy = Etsy(etsy_oauth_client=etsy_oauth)

def check_duplicates(tags):
    splits = tags.split(', ')
    # # for loop to iterate over words array
    words = []
    words_count = 0
    for split in splits:
        if split.lower() in words:
            print('listing_id ', listing_id, '  ','The Tag ', split,  ' is in list already')
        else:
            if words_count <= 12:
                words.append(split)
                words_count = words_count + 1
            else:
                print('to Many tags')
    # check each tag is 20 characters or less
    print('There are ', words_count, ' Tags')
    temp = []
    for word in words:

        if len(word) > 20:
            print(listing_id, ' one of the tags is to long:  ', word)
        else:
            temp.append(word)
    # rebuild tags with comma seperater
    L = temp
    finish = ",".join(str(x) for x in L)
    return finish

for index, row in df.iterrows():
     listing_id = int(row['listing_id'])

     tag = row['tags']  # array(string)
     tags = check_duplicates(tag)

     print('Tags Uploaded for listing_id ', listing_id, '  ', tags)
