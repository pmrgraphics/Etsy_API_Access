import oauth2 as oauth, urllib
import constants
import json

listing_id = 174277415
echo_base_url = 'https://openapi.etsy.com/v2/listings/'f'{listing_id}'
tags = ['Coin Cufflinks', 'coin jewelry', '97th Birthday', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1924 Farthing', 'gift from 1924', '97th for dad', '97th gift for dad', 'gift for men']
message = {'listing_id': listing_id, 'tags': tags}


api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

CONSUMER_KEY = constants.api_key
CONSUMER_SECRET = constants.shared_secret
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth.Token(key=oauth_token, secret=oauth_token_secret)
client = oauth.Client(consumer, token)


resp, content = client.request(
                echo_base_url,
                method="PUT",
                body=message,
                headers={'Content-Type':'application/x-www-form-urlencoded'},
                )

print('<status_code>', resp['status'])

print(content)
