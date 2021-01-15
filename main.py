
from requests_oauthlib import OAuth1Session
import requests
from requests_oauthlib import OAuth1
import json
import pandas as pd

etsy = OAuth1Session(client_key='yb9gwm6403ugxhgfmlknav41',
                     client_secret='7awvsg99o0')

'''offset = ['limit=100&offset=0',
        'limit=100&offset=100',
        'limit=100&offset=200',
        'limit=100&offset=300',
        'limit=100&offset=400',
        'limit=100&offset=500',
        'limit=100&offset=600']

for number in offset:'''

response = etsy.get("https://openapi.etsy.com/v2/shops/OldCoinCufflinks/listings/active?limit=100&offset=100&api_key=yb9gwm6403ugxhgfmlknav41")


'''response = "https://openapi.etsy.com/v2/shops/OldCoinCufflinks/listings/active?api_key=yb9gwm6403ugxhgfmlknav41"'''

user_data = response.json()

with open('personal.json') as project_file:
    data = json.load(project_file)

'''df = pd.json_normalize(data)

output = df.to_csv('etsy_listings.csv')'''


print(user_data)


