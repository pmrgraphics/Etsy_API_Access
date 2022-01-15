import mws
import os
import constants


orders_api = mws.Inventory(
        access_key=constants.AWS_Access_Key_ID,
        secret_key=constants.AWS_Client_Secret,
        account_id=constants.Seller_id,
        auth_token='amzn.mws.4cb1cb86-dc5d-04e9-87e7-b3aa79b162ec',
        region=constants.region

        )
# resp = orders_api.list_order_items(all)
orders_api.list_inventory_supply()
# service_status = orders_api.get_service_status()
# print(service_status)
# print(service_status.original)
# print(service_status.parsed)
# print(service_status.response)
