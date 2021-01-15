import json
import requests
import csv
from requests_oauthlib import OAuth1Session

etsy = OAuth1Session(client_key='yb9gwm6403ugxhgfmlknav41',
                     client_secret='7awvsg99o0')
output_file = 'etsy_listings.csv'
api_key = 'yb9gwm6403ugxhgfmlknav41'
params = {'limit': 100, 'offset': 0}
url_path = 'https://openapi.etsy.com/v2/shops/OldCoinCufflinks/listings/active?api_key=yb9gwm6403ugxhgfmlknav41'

# get data from API, parse to JSON
data = etsy.get(url_path, params=params)
data_parsed = data.json()
length_data = len(data_parsed) - 1

data_to_file = open(output_file, 'w', newline='')
csv_writer = csv.writer(data_to_file, delimiter=";")
csv_writer.writerow(["listing_id","title","price","quantity","tags","materials","occasion","style","taxonomy_id","taxonomy_path"])

for i in range(0, length_data):
    meetup = data_parsed[i]
    listing_id = meetup['listing_id']
    title = meetup['title']
    price = meetup['price']
    quantity = meetup['quantity']
    tags = meetup['tags']
    materials = meetup['materials']
    occasion = meetup['occasion']
    style = meetup['style']
    taxonomy_id = meetup['taxonomy_id']
    taxonomy_path = meetup['taxonomy_path']

    csv_writer.writerow([listing_id, title, price, quantity, tags, materials, occasion, style, taxonomy_id, taxonomy_path])
data_to_file.close()

print(data)