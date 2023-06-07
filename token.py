import requests
 url = 'https://api.github.com/authorizations'
headers = {'Authorization': 'Basic your_username:your_password'}
data = '{"scopes":["repo"],"note":"Token for accessing GitHub via API"}'
 response = requests.post(url, headers=headers, data=data)
 if response.status_code == 201:
    token = response.json()['token']
    print(f"Your token is: {token}")
else:
    print(f"Failed to create token. Status code: {response.status_code}")