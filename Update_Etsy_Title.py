from etsy2 import Etsy
from etsy2.oauth import EtsyOAuthClient
import constants

api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy_oauth = EtsyOAuthClient(client_key=api_key,
                            client_secret=shared_secret,
                            resource_owner_key=oauth_token,
                            resource_owner_secret=oauth_token_secret)

etsy = Etsy(etsy_oauth_client=etsy_oauth)

r = etsy.updateListing(listing_id=174277415, tags='Coin Cufflinks, coin jewelry, 97th Birthday, antique cufflinks, Anniversary Cufflink, 1924 Farthing, gift from 1924, 97th for dad, 97th gift for dad, gift for men')

print(r)


