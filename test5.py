import oauth2 as oauth, urllib
import constants

import urllib.parse

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



http_headers = {'Content-Type':'application/x-www-form-urlencoded'}

listing_id = 174277415
user_id = 17905617

tags = ['Coin Cufflinks', 'coin jewelry', '97th Birthday', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1924 Farthing', 'gift from 1924', '97th for dad', '97th gift for dad', 'gift for men']

materials = ['1924 Farthing', 'cufflinks', '1924 Farthing Coins']

# MESSAGE = {'tags': tags, 'materials': materials}
MESSAGE = {'listing_id': listing_id, "user_id": user_id, 'tags': tags, 'materials': materials}


def oauth_req(url, key, secret, http_method="Put", post_body=None, http_headers=None):
    CONSUMER_KEY = constants.api_key
    CONSUMER_SECRET = constants.shared_secret
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request(
        url,
        method=http_method,
        # body=str(post_body).encode('utf-8'),
        body=urllib.parse.quote(str(post_body), encoding='utf-8'),
        headers=http_headers
    )
    return content

try:
    result = oauth_req('https://openapi.etsy.com/v2/listings/%s?' % (listing_id), constants.oauth_token,
                       constants.oauth_token_secret, post_body=MESSAGE, http_headers=http_headers)

except Exception as e:
    logging.error("Exception occurred", exc_info=True)

print(result)

