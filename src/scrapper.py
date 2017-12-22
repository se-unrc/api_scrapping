import requests

# Configurations
url = 'http://localhost'
port = '4567'
headers = {}

path = "/api/pets"
payload = { 'name' : 'Nazareno' }

# res = requests.post(url + ':' + port + path, data=payload, headers=headers)
res = requests.get(url + ':' + port + path, data=payload, headers=headers)

print res.headers
print res.status_code
print res.content
