import validators
import requests
import re

# Про передачу параметров
r = requests.get('https://api.openbrewerydb.org/breweries?per_page=1')

print("\n------- status/headers/encoding ---------")

print(r.status_code)
print('content-type =>', r.headers['content-type'])
print('Content-Encoding =>', r.headers['Content-Encoding'])
print('Server =>', r.headers['Server'])
print('Cache-Control =>', r.headers['Cache-Control'])
print(r.encoding)

print("\n----------------- text ------------------")
print(r.text)
print("\n----------------- json ------------------")

print(r.json())
print('len = ', len(r.json()))
# print(r.json().get('message'))
# print(type(r.json().get('message')))
# print(validators.url(r.json().get('message')))

print("\n---------------- headers ----------------")

print(r.headers)
for key, value in r.headers.items():
    print(key, ' => ', value)


