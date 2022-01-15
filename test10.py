from urllib.parse import urlencode
from uuid import uuid4
import base64
import hashlib
import os
import re
from flask import Flask, request, session
import requests
from base64 import b64encode
from os import urandom
import constants

app = Flask(__name__)

# scope = urlencode({'scope': 'listings_d listings_r listings_w transactions_r transactions_w'})
scope = ({'scope': 'listings_d listings_r listings_w transactions_r transactions_w'})

API_BASE = 'https://www.etsy.com/'
# API_BASE = 'https://openapi.etsy.com/v3/public'
API_BASE_TOKEN = 'https://openapi.etsy.com/v3/public'
CLIENT_ID = constants.api_key
CLIENT_SECRET = constants.shared_secret
REDIRECT_URI = 'https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/'
HEADER = {"x-api-key": CLIENT_ID}

@app.route('/')
def index():
    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8')
    code_verifier = re.sub('[^a-zA-Z0-9]+', '', code_verifier)
    code_verifier, len(code_verifier)
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8')
    code_challenge = code_challenge.replace('=', '')
    code_challenge, len(code_challenge)

    params = { 'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': scope,
        'state': uuid4().hex,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256',
        'header': HEADER}

    connect_url = API_BASE + 'oauth/connect?' + urlencode({

        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': scope,
        'state': uuid4().hex,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256',
        'header': HEADER


    })

    print(connect_url)
    print(code_verifier)


    # session['code_verifier'] = code_verifier
    # session.modified = True


    return '<html><a href=%s>Connect with Etsy</a></html>' % connect_url



@app.route('/redirect')
def redirect_handler():
    assert 'error' not in request.args, request.args

    # in the real world we should validate that `state` matches the state we set before redirecting the user
    state = request.args.get('state')

    # using the code we've just been given, make a request to obtain
    # an access token for this user
    # code = request.args.get('code')
    code = 'nir19tzr3amtxeklubhqf6zntioow6vz5a0_eeg6ofopzgnhm8cxpzbni-khyfawit3byoe8mwtkktx0v4jees8aldhcfczs80oy'
    response = requests.post(API_BASE_TOKEN + '/oauth/token/', data={
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
    })
    assert response.ok, 'Token request failed: %s' % response.content

    data = response.json()
    token = data['access_token']
    headers = {
        'Authorization': 'Bearer %s' % token,
    }

    # now we can make API requests using this token in the headers
    response = requests.post(API_BASE + '/graphql', json={
        'query': '''
            query {
                user {
                    email
                }
            }
        '''
    }, headers=headers)

    assert response.ok, 'Request to graphql API failed'

    email = response.json()['data']['user']['email']
    return '''
        <html>
        %s has authorised their Marvel account
        Their access token is %s
        </html>
    ''' % (email, token)


if __name__ == '__main__':
    app.run(debug=True)