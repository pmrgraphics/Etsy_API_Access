
from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd

api_key = 'yb9gwm6403ugxhgfmlknav41'
shared_secret = '7awvsg99o0'
oauth_token = '744c77518995ae3611a0d40269f5d9'
oauth_token_secret = '05e9b62375'

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


# Creat empty List
user_data = []

limit = 100
offset = [0, 100, 200, 300, 400, 500, 600]


for number in offset:
    params = {'limit': limit, 'offset': number}
    response = etsy.get("https://openapi.etsy.com/v2/shops/OldCoinCufflinks/listings/active?", params=params)
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
print(df)

df.to_csv('etsy_listings.csv')








