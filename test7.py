
from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd

import constants



# Making data frame from the csv file
def clean(shop_name):

    df = pd.read_csv(f'{shop_name}.csv')


    column_to_replace = ("tags",
                         "materials",
                         "style",
                         )

    data = {"[": "",
            "',": ",",
            ", '": ", ",
            "]": "",
            "'": ""
            }


    # this will replace "Boston Celtics" and "Texas" with "Omega Warrior"
    def replace(column_to_replace, replace_from, replace_to):
        df[column_to_replace] = df[column_to_replace].str.replace(replace_from, replace_to, regex=True)

        return df


    for column in column_to_replace:
        # next loop for dictionary here
        for x, y in data.items():
            replace_from = x
            replace_to = y
            replace(column, replace_from, replace_to)


    output = df.to_csv("oldCoinCufflinks_clean.csv")
    return output




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


response = get_shop('OldCoinCufflinks')
cleaned = clean('OldCoinCufflinks')

print(response)
print(cleaned)








