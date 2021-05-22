import requests
from msal import PublicClientApplication

# Register your app in Azure AD to get an application ID
client_id = '90450c56-a874-4ab6-a5d6-6cb153f57905'
# If you register your app for any organization, leave as common
# If you register it for only users in your organization, change to
# your tenant ID
tenant_id = '796081d6-7a16-4179-aff9-58cfa19a9d4b'
# Array of Microsoft Graph scopes you need
scopes = [ 'User.Read', 'Calendars.Read' ]

if __name__ == '__main__':
  # Create MSAL public client
  app = PublicClientApplication(
    client_id,
    authority = 'https://login.microsoftonline.com/{0}'.format(tenant_id))

  result = None
  # Check for accounts in cache
  accounts = app.get_accounts()
  if accounts:
    # For simplicity use the first account
    user_account = accounts[0]
    # Acquire the token silently
    result = app.acquire_token_silent(scopes, user_account)

  if not result:
    # No accounts in the cache, get a token interactively
    result = app.acquire_token_interactive(scopes)

  if 'access_token' in result:
    access_token = result['access_token']

    user_response = requests.get(
      'https://graph.microsoft.com/v1.0/me',
      headers = {
        'Authorization': 'Bearer {0}'.format(access_token)
      }
    )

    user = user_response.json()
    if 'displayName' in user:
      print('Hello {0}'.format(user['displayName']))
    else:
      print(user)


    calendar_response = requests.get(
      'https://graph.microsoft.com/v1.0/me/calendarView',
      headers = {
        'Authorization': 'Bearer {0}'.format(access_token)
      },
      params = {
        'startDateTime': '2021-05-03T00:00:00Z',
        'endDateTime': '2021-05-10T00:00:00Z',
        '$select': 'subject, start, end'
      }
    )

    print(calendar_response.json())


  else:
    print(result.get('error'))
    print(result.get('error_description'))
    print(result.get('correlation_id'))
