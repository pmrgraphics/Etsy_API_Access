from etsy2 import Etsy
from etsy2.oauth import EtsyOAuthClient
import constants

from requests.exceptions import HTTPError
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy_oauth = EtsyOAuthClient(client_key=api_key,
                            client_secret=shared_secret,
                            resource_owner_key=oauth_token,
                            resource_owner_secret=oauth_token_secret)

etsy = Etsy(etsy_oauth_client=etsy_oauth)

listing_id = 940989316
tag = 'Cufflinks, Coin Cufflinks, 1971 Birthday Gift, 1971 Coin Gift, 50th Birthday, 50th Anniversary, 50th Gift, 50th Birthday Gift, 50th Birthday Him, 1971 Halfpenny, 50th Gift Dad, 50th Gift Brother, 50th Gift Husband'

try:
    r = etsy.updateListing(listing_id=listing_id,
                           tags=tag)

except HTTPError as http_err:
    logging.error("Exception occurred", exc_info=True)
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    logging.error("Exception occurred", exc_info=True)
    print(f'Other error occurred: {err}')
else:
    print(r)






