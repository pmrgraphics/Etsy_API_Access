
from requests_oauthlib import OAuth1Session
import json
from time import sleep
import pandas as pd


etsy = OAuth1Session(client_key='yb9gwm6403ugxhgfmlknav41',
                     client_secret='7awvsg99o0')

# Creat empty List
user_data = []

limit = 100
offset = [0, 100, 200, 300, 400, 500, 600]


for number in offset:
    params = {'limit': limit, 'offset': number}
    response = etsy.get("https://openapi.etsy.com/v2/shops/OldCoinCufflinks/listings/active?api_key=yb9gwm6403ugxhgfmlknav41", params=params)
    sleep(0.5)
    user_data.append(response.json())

# Opening JSON file
with open('personal.json', 'w') as json_file:
    json.dump(user_data, json_file)

print('Type: ', type(user_data))


'''def return_listings(response):
    results = response['results']

    listings = []
    for item in results:
        listing = {}
        listing['url'] = item['url']
        listing['title'] = item['title']
        listings.append(listing)

    return {'listings': listings}

print(return_listings(user_data))'''

# Opening JSON file


# load data using Python JSON module
with open('personal.json', 'r') as f:
    data = json.loads(f.read())

# Normalizing data
df = pd.json_normalize(data, record_path=['results'])
print(df)

df.to_csv('etsy_listings.csv')




df.to_json('backtojson.json')




