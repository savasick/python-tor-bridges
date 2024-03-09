import requests

response = requests.get('https://check.torproject.org/')

print(response.text)
