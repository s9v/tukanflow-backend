import requests
import json
import yaml

from auth import get_token_from_code

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  # Send GET to /me
  user = requests.get(
    '{0}/me'.format(graph_url),
    headers={
      'Authorization': 'Bearer {0}'.format(token)
    },
    params={
      '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
    })
  # Return the JSON result
  return user.json()

REQUEST = "http://localhost:8000/callback?code=M.R3_BAY.f06c344e-a98a-8231-2a63-450b784abeb5&state=KfTjYvESehCmLNlW"

result = get_token_from_code(REQUEST)
print(result)
