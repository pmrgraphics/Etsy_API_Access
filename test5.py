from time import sleep
from ebaysdk.trading import Connection as trading
import pandas as pd
from glom import glom
from ast import literal_eval


api = trading(
    appid="PaulRead-replacme-PRD-1c2490906-7d7150ee", devid="e3b3d2c0-38f4-4997-b251-9fb8c5922fd3",
    certid="PRD-c24909065239-cd6b-41a1-93a3-2ae3",
    token="AgAAAA**AQAAAA**aAAAAA**FRjXYQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wJnY+jCJaKpgqdj6x9nY+seQ**xt4GAA**AAMAAA**89hWZlRIaK+tOsoKEaKv0pNiuAyk/Ov9l7a26YJvs6+uq66Fkc07VL/kbFUR/GJCydLAa/1EARG4+nVXAkXz6Ke9rL5pVKOH+TXCduDEFwdtCq0XzBqZCeHf6+Z8+tT9FLk17NAAIvLjf7qN+j31wve3RPe0QAGKG6X2eCVFJP2XhvYR4ZQyicVRrbkujiQ9vONXqo6YJpO51em+NWzngcCZfGqwRRoNaD+jJ0sSgVy4qMIxV/LuJnHlKOdbgV8EIdLE4rxa9iEfs8T5dOl2MBj1oDEcPM/ln66AkgtfasFxQuwVB59LEonkARDzXvk0eEqzV8VgVP8TW6f0iCmTWKEhkBSP71JVQetKd/ggXDJV/8+JSxHGxhT6iH7u3i3M0yJqQEN7CuxvHGtO3eaQQsAR5jjF1a6IGeNgM+NWHYeNIji5zRm1rxpBarsIu3Z+12FFzbec9XvltePoHj9BIvg8TgNVBWuk4eNoZ0s3Aysx05byo6qtvH3fUR0MV3aY88LtrBwXVjeLbsOVz2J/KKwXZ4YMrmTAo49K5mjdVkcVti/vTw/qzzO/m0GyRhJXfmDDsnEOZOORjk8uw6ndX0XwOsyh92UEuRgp2WmJYhy5uUVJZi+eoWTcT7YuwCVuacucBtxBcGOeLh2K39hdditpV9DauJAVgalsFnI69H9l6bqh2pn3dH+gHeeMJsgO0EJZ+7cnRUtouxh4kOf4OOZjepqY0j5mQev6SidrP07PERE9K+QcY0FrFFhUgbgy")
if True:
    ebay_df = pd.read_csv('output_ebay_test.csv')
    for index, row in ebay_df.iterrows():
        ebay_item_no = row['ItemId']
        ebay_title = row['Title']
        ebay_description = row['Description']

        # print(ebay_item_no,ebay_title, ebay_description)

        #
        api.execute('ReviseFixedPriceItem', {'item': {'ItemID': ebay_item_no, 'Title': ebay_title, 'Description': "<![CDATA[{0}]]>".format(ebay_description)}})
        sleep(0.2)
        response_r = api.response_content()
        print(response_r)


