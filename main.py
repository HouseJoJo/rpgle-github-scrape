import requests

url = 'https://api.github.com'
headers = {'Authorization': 'Bearer AUTH_TOKEN'}
response = requests.get(url, headers=headers)
print(response.status_code)

if response.status_code == 200:
    json_data = response.json()
    print(json_data['organizational_url'])

