import os
import datetime
import pandas as pd
import sys
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

# API key is set in .env file - create and save in same directory
from dotenv import load_dotenv

load_dotenv()
# API_KEY = os.getenv('api_key')
API_KEY = 'PaulRead-replacme-PRD-1c2490906-7d7150ee'



class Ebay_21(object):
    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def fetch(self):
        try:
            # api = Connection(domain='svcs.sandbox.ebay.com',config_file="ebay.yaml", siteid="EBAY-GB")
            api = Connection(config_file="ebay.yaml", siteid="EBAY-GB")
            # response = api.execute('findItemsIneBayStores', {'storeName': 'rstrading'})
            response = api.execute('findItemsAdvanced', {'keywords': '1962 sixpence'})

            assert (response.reply.ack == 'Success')
            assert (type(response.reply.timestamp) == datetime.datetime)
            assert (type(response.reply.searchResult.item) == list)

            print(f"Total items {response.reply.paginationOutput.totalEntries}\n")

            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                print(f"Buy it now available : {item.listingInfo.buyItNowAvailable}")
                print(f"Country : {item.country}")
                print(f"End time :{item.listingInfo.endTime}")
                print(f"URL : {item.viewItemURL}")

            assert (type(item.listingInfo.endTime) == datetime.datetime)
            assert (type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

    def get_active_listings(page):
        api = Connection(appid='PaulRead-replacme-PRD-1c2490906-7d7150ee', config_file=None, siteid="EBAY-GB")
        acitvelist = api.execute('GetMyeBaySelling', {'ActiveList': True,
                                                      'DetailLevel': 'ReturnAll',
                                                      'PageNumber': page})
        return acitvelist.dict()


# main driver
if __name__ == '__main__':


    e = Ebay_21(API_KEY)
    e.fetch()
    print(e.get_active_listings())

