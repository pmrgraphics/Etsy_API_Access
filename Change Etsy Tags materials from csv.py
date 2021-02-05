from time import sleep
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


# not_these = ['st', 'nd', 'rd', 'a', 'the', 'of']
# thestring = tags
# word =  ' '.join(word
#                if word in not_these
#                else word.title()
#                for word in thestring.capitalize().split(' '))



def check_duplicates(tags):
    # not_these = ['st', 'nd', 'rd', 'a', 'the', 'of']
    # thestring = tags
    # words = ' '.join(word
    #                if word in not_these
    #                else word.title()
    #                for word in thestring.Capitalise().split(' '))


    splits = tags.split(', ')
    # # for loop to iterate over words array
    words = []
    for split in splits:
        if split.lower() in words:
            print(split, 'in list already')
        else:
            # words.append(split.title())
            words.append(split)
    # check each tag is 20 characters or less
    temp = []
    for word in words:

        if len(word) > 20:
            print('one of the tags is to long:  ', word)
        else:
            temp.append(word)
    # rebuild tags with comma seperater
    L = temp
    finish = ",".join(str(x) for x in L)
    return finish


# go through eacjh row of the data frame and pick out requested info
for index, row in df.iterrows():
    listing_id = row['listing_id']
    title = row['title']
    tag = row['tags']
    tags = check_duplicates(tag)
    materials = row['materials']
    recipient = row['recipient']
    occasion = row['occasion']
    style = row['style']
    taxonomy_id = row['taxonomy_id']

    try:
        r = etsy.updateListing(listing_id=listing_id, title=title,
                               tags=tags, materials=materials, recipient=recipient,
                               occasion=occasion, style=style, taxonomy_id=taxonomy_id)

        # slow down so not to many hits per second on api endpoint
        sleep(0.5)

    except HTTPError as http_err:
        logging.error("Exception occurred", exc_info=True)
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error("Exception occurred", exc_info=True)
        print(f'Other error occurred: {err}')
    else:
        print(r)
















