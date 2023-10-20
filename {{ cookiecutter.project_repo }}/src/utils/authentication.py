import os
import requests
from starlette import status
from logging import logger

authentification_url=os.getenv('GEOSYS_AUTHENTICATION_URL')
if authentification_url is None:
    logger.error("GEOSYS_AUTHENTICATION_URL environment variable has not been defined")

###############################################################################
# Exchange the bearer token and get a refresh token
def token_exchange(context: dict):
    bearer = context['cloudevent_attributes']['g6bearertoken']
    authentification_url = os.getenv('GEOSYS_AUTHENTICATION_URL')
    authentification_client_id = os.getenv('GEOSYS_AUTHENTICATION_CLIENT_ID')
    authentification_client_secret = os.getenv('GEOSYS_AUTHENTICATION_CLIENT_SECRET')
    disable_ssl = os.getenv('DISABLE_SSL_VERIFICATION', default=False)

    response=requests.post(
        authentification_url + "/connect/token", data = {
            'exchange_style':'impersonation',
            'subject_token':bearer,
            'subject_token_type':'urn:ietf:params:oauth:token-type:access_token',
            'grant_type':'urn:ietf:params:oauth:grant-type:token-exchange',
            'scope':'offline_access openid',
            'client_id':authentification_client_id,
            'client_secret':authentification_client_secret
        },
        headers={
            'Accept':'*/*',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        , verify = not disable_ssl
    )
    
    if response.status_code != status.HTTP_200_OK:
        raise Exception("Error while authenticating")
    
    result=response.json()

    context['bearer_token'] = result['access_token']
    context['refresh_token'] = result['refresh_token']

###############################################################################
# Refresh the bearer token
def token_refresh(refresh_token):
    authentification_url = os.getenv('GEOSYS_AUTHENTICATION_URL')
    authentification_client_id = os.getenv('GEOSYS_AUTHENTICATION_CLIENT_ID')
    authentification_client_secret = os.getenv('GEOSYS_AUTHENTICATION_CLIENT_SECRET')
    disable_ssl = os.getenv('DISABLE_SSL_VERIFICATION', default=False)

    response=requests.post(
        authentification_url + "/connect/token", data = {
            'refresh_token':refresh_token,
            'grant_type':'refresh_token',
            'client_id':authentification_client_id,
            'client_secret':authentification_client_secret
        },
        headers={
            'Accept':'*/*',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        , verify = not disable_ssl
    )
    
    if response.status_code != status.HTTP_200_OK:
        raise Exception("Error while authenticating: " + response.text)
    
    result=response.json()
    return  result['access_token']
