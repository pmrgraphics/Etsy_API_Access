from etsy2 import Etsy
from etsy2.oauth import EtsyOAuthHelper, EtsyOAuthClient
import urllib.parse as urlparse
from urllib.parse import parse_qs

api_key = 'yb9gwm6403ugxhgfmlknav41'
shared_secret = '7awvsg99o0'

#define permission scopes
permission_scopes = ['email_r','listings_r', 'listings_w', 'listings_d', 'transactions_r', 'billing_r', 'feedback_r']

login_url, temp_oauth_token_secret = \
    EtsyOAuthHelper.get_request_url_and_token_secret(api_key, shared_secret, permission_scopes)

query = urlparse.urlparse(login_url).query
temp_oauth_token = parse_qs(query)['oauth_token'][0]

print(login_url)
#follow the url to acquire the verifier.

oauth_token, oauth_token_secret = \
    EtsyOAuthHelper.get_oauth_token_via_verifier(api_key, shared_secret, temp_oauth_token, temp_oauth_token_secret, input('Verifier: '))

etsy_oauth = EtsyOAuthClient(client_key = api_key,
                             client_secret = shared_secret,
                             resource_owner_key = oauth_token,
                             resource_owner_secret = oauth_token_secret)

etsy = Etsy(etsy_oauth_client = etsy_oauth)
print(oauth_token)
print(oauth_token_secret)

listing_data = {
            'tags': ('Sixpence Coin Cufflinks', 'coin jewelry', 'Golden Wedding Anniversary', 'antique cufflinks', 'Anniversary Cufflinks',
                     '1961', 'gift from 1961', '60th birthday for him', '60th for dad', '60th gift for dad', 'gift for men')
               }
request_url = 'https://openapi.etsy.com/v2/listings/197564673'
print(etsy.get(request_url))
print(etsy.put(request_url, listing_data))

    #currently forbidden

etsy.put(request_url, listing_data)
