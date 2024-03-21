import requests

request = requests.get('https://www.idently.io')
print(request.status_code)