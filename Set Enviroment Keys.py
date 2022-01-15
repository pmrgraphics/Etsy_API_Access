from os import environ as env
import os
import constants
import json

# os.environ['client_key'] = constants.api_key
# os.environ['client_secret'] = constants.shared_secret
# os.environ['oauth_token'] = constants.oauth_token
# os.environ['oauth_token_secret'] = constants.oauth_token_secret
# os.environ['shop_id'] = constants.shop_id



def print_env():
  print(json.dumps({**{}, **os.environ}, indent=2))

print(print_env())