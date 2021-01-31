import oauth2 as oauth, urllib
import constants

import urllib.parse


http_headers = {'Content-Type':'application/x-www-form-urlencoded'}

listing_id = 174277415

tags = ['Coin Cufflinks', 'coin jewelry', '97th Birthday', 'antique cufflinks', 'Anniversary Cufflinks',
                    '1924 Farthing', 'gift from 1924', '97th for dad', '97th gift for dad', 'gift for men']

materials = ['1924 Farthing', 'cufflinks', '1924 Farthing Coins']

# MESSAGE = {'tags': tags, 'materials': materials}
MESSAGE = {'listing_id': listing_id,'tags': tags, 'materials': materials}


def oauth_req(url, key, secret, http_method="PUT", post_body=None, http_headers=None):
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
        headers=http_headers,
    )

    print(resp)
    print(http_method)
    print(urllib.parse.quote(str(post_body), encoding='utf-8'))
    print(http_headers)
    return content



result = oauth_req('https://openapi.etsy.com/v2/listings/%s?'%(listing_id), constants.oauth_token, constants.oauth_token_secret, post_body=MESSAGE, http_headers=http_headers)

print(result)


