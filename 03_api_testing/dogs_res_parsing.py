import requests
import re

# Про передачу параметров
r = requests.get('https://dog.ceo/api/breed/hound/images')

# print("\n------- status/headers/encoding ---------")
#
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
#
# print("\n----------------- text ------------------")
# print(r.text)
# print("\n----------------- json ------------------")
#
# print(r.json())
# print(type(r.json().get('message')))
#
# print("\n---------------- headers ----------------")
#
# for key, value in r.headers.items():
#     print(key, ' => ', value)

prog = re.compile(r'^https://images.dog.ceo/breeds/hound-afghan.*')

links_list = r.json().get("message")
print(links_list)
for link in links_list:
    x = prog.match(link)
    if x is None:
        continue
    print(x.group(0))
    # if link.startswith('https://images.dog.ceo/breeds/hound-afghan/'):
    #     print(link)


