import boto3
import constants
# ======== GET AUTH ========
# Credentials for user created following the docs
amw_client = boto3.client(
    'sts',
    aws_access_key_id=constants.AWS_Access_Key_ID,
    aws_secret_access_key=constants.AWS_Client_Secret,
    region_name='UK'
)
# ROLE created following the docs
# STS assume policy must be included in the role
res = amw_client.assume_role(
    RoleArn='arn:aws:iam::600751160541:user/paulr@rstrading.co.uk',
    RoleSessionName='SellingPartnerAPI'
)

Credentials = res["Credentials"]
AccessKeyId = Credentials["AccessKeyId"]
SecretAccessKey = Credentials["SecretAccessKey"]
SessionToken = Credentials["SessionToken"]

from requests_auth_aws_sigv4 import AWSSigV4

aws_auth = AWSSigV4('execute-api',
                    aws_access_key_id=constants.AWS_Access_Key_ID,
                    aws_secret_access_key=constants.AWS_Client_Secret,
                    aws_session_token=SessionToken,
                    region='UK'
                    )

import requests

request_url = 'https://sellingpartnerapi-eu.amazon.com'

# ======== CONSUME API ========
resp = requests.get(
request_url, headers=aws_auth)

print(resp.json())
