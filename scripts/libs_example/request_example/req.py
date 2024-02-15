import requests

url = 'https://yandex.ru'
# headers = {'Authorization': 'Bearer your_access_token'}

response = requests.get(url)

if response.status_code == 200:
    #data = response.json()
    print(response.headers['content-type'])
else:
    print('Failed to fetch data. Status code:', response.status_code)
