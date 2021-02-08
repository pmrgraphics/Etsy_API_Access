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


# go through each row of the data frame and pick out requested info
for index, row in df.iterrows():
     listing_id = int(row['listing_id'])
     quantity = int(row['quantity'])  # int
     title = row['title']  # string
     description = row['description']  # text
     price = row['price']  # float
     materials = row['materials']  # array(string)
     shipping_template_id = int(row['shipping_template_id'])  # int
     taxonomy_id = int(row['taxonomy_id'])  # int
     tag = row['tags']  # array(string)
     tags = check_duplicates(tag)
     who_made = row['who_made']  # enum(i_did, collective, someone_else)
     # is_supply = ['is_supply']  # boolean
     when_made = ['when_made']  # enum(made_to_order, 2020_2021, 2010_2019, 2002_2009, before_2002, 2000_2001, 1990s, 1980s, 1970s, 1960s, 1950s, 1940s, 1930s, 1920s, 1910s, 1900s, 1800s, 1700s, before_1700)
     recipient = row['recipient']  # enum(en, women, unisex_adults, teen_boys, teen_girls, teens, boys, girls, children, baby_boys, baby_girls, babies, birds, cats, dogs, pets, not_specified))
     occasion = row['occasion']  # enum(anniversary, baptism, bar_or_bat_mitzvah, birthday, canada_day, chinese_new_year, cinco_de_mayo, confirmation, christmas, day_of_the_dead, easter, eid, engagement, fathers_day, get_well, graduation, halloween, hanukkah, housewarming, kwanzaa, prom, july_4th, mothers_day, new_baby, new_years, quinceanera, retirement, st_patricks_day, sweet_16, sympathy, thanksgiving, valentines, wedding)
     style = row['style']  # array(string)
     image_name = row['image_name']
     image_location = row['image_location']



     try:
        r = etsy.updateListing(listing_id=listing_id, quantity=quantity, title=title, description=description,
                               price=price, tags=tags, materials=materials, recipient=recipient,
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

        response = OAuth1Session(client_key=api_key,
                                 client_secret=shared_secret,
                                 resource_owner_key=oauth_token,
                                 resource_owner_secret=oauth_token_secret)


        listing_image_id = 1
        os.chdir('/Users/paulread/PycharmProjects/Etsy API Access/images')
        uri = 'https://openapi.etsy.com/v2/listings/%s/images' % listing_id
        files = {'image': (
             f'{image_name}', open(f'{image_location}', 'rb'),
             'image/jpeg')}
        params = {'listing_id': f'{listing_id}', 'listing_image_id': 1}
        result = response.post(uri, params=params, files=files)
















