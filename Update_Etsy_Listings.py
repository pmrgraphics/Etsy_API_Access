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
    # print('There are ', words_count, ' Tags')
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



# go through each row of the data frame and pick out requested info
for index, row in df.iterrows():
     listing_id = int(row['listing_id'])
     title = row['title']  # string
     description = row['description']  # text
     price = row['price']  # float - Remove when updating Variants
     materials = row['materials']  # array(string)
     taxonomy_id = int(row['taxonomy_id'])  # int
     tag = row['tags']  # array(string)
     tags = check_duplicates(tag)
     # recipient = row['recipient']  # enum(en, women, unisex_adults, teen_boys, teen_girls, teens, boys, girls, children, baby_boys, baby_girls, babies, birds, cats, dogs, pets, not_specified))
     # occasion = row['occasion']  # enum(anniversary, baptism, bar_or_bat_mitzvah, birthday, canada_day, chinese_new_year, cinco_de_mayo, confirmation, christmas, day_of_the_dead, easter, eid, engagement, fathers_day, get_well, graduation, halloween, hanukkah, housewarming, kwanzaa, prom, july_4th, mothers_day, new_baby, new_years, quinceanera, retirement, st_patricks_day, sweet_16, sympathy, thanksgiving, valentines, wedding)
     # style = row['style']  # array(string)

     try:
        r = etsy.updateListing(listing_id=listing_id,  title=title, description=description,
                               price=price,tags=tags, materials=materials, taxonomy_id=taxonomy_id)

        # slow down so not to many hits per second on api endpoint
        sleep(0.2)

     except HTTPError as http_err:
        logging.error("Exception occurred", exc_info=True)
        print(f'HTTP error occurred: {http_err}')
     except Exception as err:
        logging.error("Exception occurred", exc_info=True)
        print(f'Other error occurred: {err}')
        #TODO Code to Write Reason and Listing_id to File?

        # TODO Other error occurred: Could not decode response from Etsy as JSON: status_code: 403, text: 'listing inventory is not backwards compatible, cannot manually set price or quantity', url 'https://openapi.etsy etc etc
        # when this happens do not update price

        # TODO Other error occurred: Could not decode response from Etsy as JSON: status_code: 400, text: 'You may not have duplicate tags.', url 'https://openapi.etsy.com/v2/listings/185224429'
     else:
        print(r)



















