
from requests_oauthlib import OAuth1Session

api_key = 'yb9gwm6403ugxhgfmlknav41'
shared_secret = '7awvsg99o0'
oauth_token = '744c77518995ae3611a0d40269f5d9'
oauth_token_secret = '05e9b62375'

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


data = {
            'tags': ['Sixpence Coin Cufflinks', 'coin jewelry', 'Golden Wedding Anniversary', 'antique cufflinks', 'Anniversary Cufflinks',
                     '1961', 'gift from 1961', '60th birthday for him', '60th for dad', '60th gift for dad', 'gift for men'],
            'materials': ['1961 lucky Sixpence', 'cufflinks', 'french cufflink backs', 'Gold Plated cuff links', '1961 Lucky Sixpence Coins']
         }


print(etsy.put('https://openapi.etsy.com/v2/listings/197564673',
               params=data))
