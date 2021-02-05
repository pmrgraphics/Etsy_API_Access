from requests_oauthlib import OAuth1Session
import os
import constants
api_key = constants.api_key
shared_secret = constants.shared_secret
oauth_token = constants.oauth_token
oauth_token_secret = constants.oauth_token_secret

etsy = OAuth1Session(client_key=api_key,
                     client_secret=shared_secret,
                     resource_owner_key=oauth_token,
                     resource_owner_secret=oauth_token_secret)


response = [{'listing_id': 943096360,
     'state': 'active',
     'user_id': 17905617,
     'category_id': None,
     'title': 'Premium 1961 Sixpence Cufflinks 60th birthday. 1961 gift for dad, 60th gift for him, grandad gift 60th, 6d, Sixpence Coin, 60th Brother - HT',
     'description': '1961 Birthday Cufflinks 60th birthday cufflinks\n\n1961 Sixpence cufflinks for sale\n\nGenuine 1961 Circulated 60 year old Sixpence\n\nA great gift for 60th Birthday / Anniversary \n\nSupplied in a nice cufflink box',
     'creation_tsz': 1612530558,
     'ending_tsz': 1622894958,
     'original_creation_tsz': 1612530558,
     'last_modified_tsz': 1612530559,
     'price': '29.98',
     'currency_code': 'USD',
     'quantity': 10,
     'sku': [],
     'tags': ['1961 coin gift', '1961 gift', '1961 birthday', '1961 birthday gift', 'born in 1961', 'fathers day', '1961 Gift Idea', 'Gift for him', 'Gift for Dad', '60th birthday', '60th for dad', '60th Present', '60th gift for dad'],
     'materials': ['1961 Silver Sixpence', 'Cuff Link Box'],
     'shop_section_id': None,
     'featured_rank': None,
     'state_tsz': 1612530558,
     'url': 'https://www.etsy.com/listing/943096360/premium-1961-sixpence-cufflinks-60th?utm_source=bulkupload&utm_medium=api&utm_campaign=api',
     'views': 0,
     'num_favorers': 0,
     'shipping_template_id': 40038938742,
     'processing_min': 1,
     'processing_max': 2,
     'who_made': 'i_did',
     'is_supply': 'false',
     'when_made': 'made_to_order',
     'item_weight': None,
     'item_weight_unit': None,
     'item_length': None,
     'item_width': None,
     'item_height': None,
     'item_dimensions_unit': None,
     'is_private': False,
     'recipient': 'men',
     'occasion': 'birthday',
     'style': ['Traditional'],
     'non_taxable': False,
     'is_customizable': True,
     'is_digital': False,
     'file_data': '',
     'can_write_inventory': True,
     'should_auto_renew': False,
     'language': 'en-US',
     'has_variations': False,
     'taxonomy_id': 52,
     'taxonomy_path': ['Accessories', 'Suit & Tie Accessories', 'Cuff Links & Tie Clips', 'Cuff Links'],
     'used_manufacturer': False,
     'is_vintage': False,
     'ShippingInfo': [{'shipping_info_id': 24681774808, 'origin_country_id': 105, 'destination_country_id': 105, 'currency_code': 'USD', 'primary_cost': '0.00', 'secondary_cost': '0.00', 'listing_id': 943096360, 'region_id': None, 'origin_country_name': 'United Kingdom', 'destination_country_name': 'United Kingdom'},
                      {'shipping_info_id': 24681103229, 'origin_country_id': 105, 'destination_country_id': 209, 'currency_code': 'USD', 'primary_cost': '2.00', 'secondary_cost': '0.00', 'listing_id': 943096360, 'region_id': None, 'origin_country_name': 'United Kingdom', 'destination_country_name': 'United States'},
                      {'shipping_info_id': 24681103223, 'origin_country_id': 105, 'destination_country_id': 61, 'currency_code': 'USD', 'primary_cost': '2.00', 'secondary_cost': '0.00', 'listing_id': 943096360, 'region_id': None, 'origin_country_name': 'United Kingdom', 'destination_country_name': 'Australia'},
                      {'shipping_info_id': 24681103215, 'origin_country_id': 105, 'destination_country_id': None, 'currency_code': 'USD', 'primary_cost': '2.00', 'secondary_cost': '0.00', 'listing_id': 943096360, 'region_id': None, 'origin_country_name': 'United Kingdom', 'destination_country_name': 'Everywhere Else'}]}]


my_dict = response[0].items()

print(my_dict)

#
# function to return key for any value
def get_key(val):
    for key, value in my_dict:
        if key == key:
            return value

    return "key doesn't exist"

print(get_key('listing_id'))

listing_id = get_key('listing_id')
listing_image_id = 1
os.chdir('/Users/paulread/PycharmProjects/Etsy API Access/images')
uri = 'https://openapi.etsy.com/v2/listings/%s/images'%listing_id
files = {'image': ("Premium 1961 Sixpence Cullink Rose Gold.jpg'", open('Premium 1961 Sixpence Cullink Rose Gold.jpg', 'rb'), 'image/jpeg')}
params = {'listing_id':f'{listing_id}', 'listing_image_id': 1}
result = etsy.post(uri, params=params, files=files)
#
#
# images = ['Premium 1961 Sixpence Cullink Rose Gold.jpg', open('Premium 1961 Sixpence Cullink Rose Gold.jpg', 'rb', 'image/jpg' )]
#
#
# try:
#
#     r = etsy.uploadListingImage(listing_id=listing_id, listing_image_id=listing_image_id, images=images, headers={'Content-Type': 'multipart/form-data'})
#
#     # slow down so not to many hits per second on api endpoint
#     sleep(0.5)
#
# except HTTPError as http_err:
#     logging.error("Exception occurred", exc_info=True)
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     logging.error("Exception occurred", exc_info=True)
#     print(f'Other error occurred: {err}')
# else:
#     print(r)
# #
# #
# #
# #
# #














