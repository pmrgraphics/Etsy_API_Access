
from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd

import constants
import log

@log.log_error()
def get_shop(shop):
    api_key = constants.api_key
    shared_secret = constants.shared_secret
    oauth_token = constants.oauth_token
    oauth_token_secret = constants.oauth_token_secret

    etsy = OAuth1Session(client_key=api_key,
                         client_secret=shared_secret,
                         resource_owner_key=oauth_token,
                         resource_owner_secret=oauth_token_secret)


    # Creat empty List
    user_data = []

    limit = 100
    offset = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
    shop_name = f'{shop}'

    for number in offset:
        params = {'limit': limit, 'offset': number}
        response = etsy.get("https://openapi.etsy.com/v2/shops/%s/listings/active?"%(shop_name), params=params)
        sleep(0.5)
        user_data.append(response.json())

    # Opening JSON file
    with open('personal.json', 'w') as json_file:
        json.dump(user_data, json_file)

    print('Type: ', type(user_data))




    # load data using Python JSON module
    with open('personal.json', 'r') as f:
        data = json.loads(f.read())

    # Normalizing data
    df = pd.json_normalize(data, record_path=['results'])

    df.to_csv(f'{shop_name}.csv')
    return df


response = get_shop('AcmeCufflinks')
print(response)








