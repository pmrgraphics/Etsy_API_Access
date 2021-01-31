
from etsy2 import Etsy
from etsy2.oauth import EtsyOAuthClient
import constants
import json

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy_oauth = EtsyOAuthClient(client_key=api_key,
                            client_secret=shared_secret,
                            resource_owner_key=oauth_token,
                            resource_owner_secret=oauth_token_secret)
etsy = Etsy(etsy_oauth_client=etsy_oauth)

listing_id = 174277415

url = 'https://openapi.etsy.com/v2/listings/'f'{listing_id}'

headers={'Content-Type':'application/x-www-form-urlencoded'}

tags = {'Coin Cufflinks', 'coin jewelry', '97th Birthday', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1924 Farthing', 'gift from 1924', '97th for dad', '97th gift for dad', 'gift for men'}
message = {'listing_id': listing_id, 'tags': tags}

r = etsy.updateListing(listing_id=174277415, title='1924 97th Birthday Anniversary Farthing coin with a Silver Plated Pendant mount 97th birthday gift for her')
print(r)

for each in tags:
    print(len(each))
