
from requests_oauthlib import OAuth1Session
import json
from time import sleep


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



# Opening JSON file









