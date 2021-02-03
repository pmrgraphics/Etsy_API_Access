from oauthlib.oauth1 import SIGNATURE_TYPE_BODY
import requests
from requests_oauthlib import OAuth1Session

api_key = 'yb9gwm6403ugxhgfmlknav41'
shared_secret = '7awvsg99o0'
oauth_token = '4f35e454d103084943206de54f4577'
oauth_token_secret = '38210c773f'


etsy = OAuth1Session(client_key=api_key,
                    client_secret=shared_secret,
                    resource_owner_key=oauth_token,
                    resource_owner_secret=oauth_token_secret,
                    # signature_type='body'
                    # force_include_body=True,
                    # signature_type='body'
                    )

headers = {'Content-Type':'application/x-www-form-urlencoded'}


listing_data = {'tags': ['Sixpence Coin, coin jewelry, Golden Wedding, antique cufflinks, Anniversary Cufflinks, 1961, gift from 1961, 60th for him, 60th for dad, 60th gift for dad, gift for men'],
'materials': ['1961 lucky Sixpence, cufflinks, french cufflink backs, Gold Plated cuff links, 1961 Lucky Sixpence Coins'],
               }

url = 'https://openapi.etsy.com/v2/listings/197564673?'



result = etsy.put(url, data=listing_data)
print(result.status_code)

response = etsy.get("https://openapi.etsy.com/v2/oauth/scopes")
print(response.json())
print(result.status_code)
print(result.text)
print(result.headers)
print(result.url)
print(result.content)
print(result.reason)



