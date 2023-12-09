#!/usr/bin/env python3
import sys
import os
import json
import pynetbox

file = '.nb_config.json'

path = os.path.abspath(f'{file}')

n = open(f'{path}')

data = json.load(n)

nb_url = data['url']
nb_api_token = data['token']

if not nb_url:
    print("netbox url variable nb_url is not set")
    sys.exit()

if not nb_api_token:
    print("netbox api token variable nb_api_token is not set")


nb = pynetbox.api(
    f'{nb_url}',
    token=f'{nb_api_token}'
)

#response = nb.ipam.vlans.get()

#print(response)
