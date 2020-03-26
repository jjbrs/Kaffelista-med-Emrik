# This file is meant to test the functionalities of the API built in this software.
# Official documentation: https://requests.readthedocs.io/en/master/
import requests
import json

# definitions of host and port
host = 'localhost'
port = 4000

fail = False # keeps track if any of the tests had failed

# step 1: get the token
reply = requests.get(f'http://{host}:{port}/api/token/public')
if reply.status_code == 200:
    print('request successful')
    auth = reply.json()
    token = auth['token']
    print('My authentication token is:', token)
else:
    print('token request was not successful')
    fail = True

# step 2: getting information about the web service

req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
               }
reply = requests.get(f'http://{host}:{port}/api/', headers=req_headers)

print('Status:', reply.status_code)

if reply.status_code == 200:
    print(reply.json())
elif reply.status_code == 403:
    print('Your credentials have expired! Get new ones!')
    fail = True

# step 3: getting a list of posts
print('\n\nGetting a list of purchases')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

reply = requests.get(f'http://{host}:{port}/api/purchases', headers=req_headers)

print('Code:', reply.status_code)

if reply.status_code == 200:
    for purchase in reply.json():
        print('Purchase', purchase['id'])
        for key, value in purchase.items():
            if key == 'content':
                print('\t', key.ljust(15), ':', value[:50].replace('\n', ''), '...')
            elif key == 'id':
                continue
            elif isinstance(value, dict):
                print('\t', key, ':')
                for k2, v2 in value.items():
                    print('\t\t', k2.ljust(15), ':', v2)
            else:
                print('\t', key.ljust(15), ':', value)
elif reply.status_code == 403:
    print('GET LIST: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('GET LIST: There was an error:', reply.status_code)
    fail = True

# step 4: inserting a new post
print('\n\nInserting a purchase')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

purchase = {'type_of_fika': 'Define here the type of fika of the student llllll',
            'user': 1}

reply = requests.purchase(f'http://{host}:{port}/api/purchase', headers=req_headers, data=json.dumps(purchase))

if reply.status_code == 201:
    print('Created with success')
    purchase_received = reply.json()
    print('Purchase created:')
    purchase_id = purchase_received['id']
    print('\tid:', purchase_received['id'])
    print('\ttitle:', purchase_received['title'])
elif reply.status_code == 403:
    print('INSERT: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('INSERT: There was an error:', reply.status_code)
    fail = True


# step 5: getting a specific post
print('\n\nGetting a purchase')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

reply = requests.get(f'http://{host}:{port}/api/purchase/{purchase_id}', headers=req_headers)

if reply.status_code == 200:
    print('Purchase found:')
    for key, value in reply.json().items():
        print('\t', key, ':', value)
elif reply.status_code == 404:
    print('FIND PURCHASE: Purchase not found! Try another id!')
    fail = True
elif reply.status_code == 403:
    print('FIND PURCHASE: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('FIND PURCHASE: There was an error:', reply.status_code)
    fail = True

# step 6: replacing a post
print('\n\nReplacing a purchase')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

purchase = {'type_of_fika': 'Define here the type of fika of the student llllll',
             'user': 1}

reply = requests.put(f'http://{host}:{port}/api/purchase/{purchase_id}', headers=req_headers, data=json.dumps(purchase))

if reply.status_code == 200:
    print('Replaced with success')
    purchase_received = reply.json()
    print('Purchase created:')
    print('\tid:', purchase_received['id'])
    print('\ttitle:', purchase_received['title'])
elif reply.status_code == 403:
    print('REPLACE: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('REPLACE: There was an error:', reply.status_code)
    print(reply.text)
    fail = True

# step 7: editing a post
print('\n\nEditing a purchase')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

purchase = {'type_of_fika': 'Define here the title of the student llllll -- replaced',
            'user': 1
             }

reply = requests.patch(f'http://{host}:{port}/api/purchaset/{purchase_id}', headers=req_headers, data=json.dumps(purchase))

if reply.status_code == 200:
    print('Updated with success')
    purchase_received = reply.json()
    print('Purchase created:')
    print('\tid:', purchase_received['id'])
    print('\ttitle:', purchase_received['title'])
elif reply.status_code == 403:
    print('UPDATE: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('UPDATE: There was an error:', reply.status_code)
    print(reply.text)
    fail = True

# step 8: deleting a post
print('\n\nDeleting a purchase')
req_headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
              }

reply = requests.delete(f'http://{host}:{port}/api/purchase/{purchase_id}', headers=req_headers)

if reply.status_code == 200:
    print('Purchase deleted:')
    for key, value in reply.json().items():
        print('\t', key, ':', value)
elif reply.status_code == 404:
    print('DELETE: Purchase not found! Try another id!')
    fail = True
elif reply.status_code == 403:
    print('DELETE: Your credentials have expired! Get new ones!')
    fail = True
else:
    print('DELETE: Unknown error:', reply.status_code)
    fail = True
    print(reply.text)


if not fail:
    print('\n\nTHE TESTS WERE SUCCESSFUL')
else:
    print('\n\nTHE TESTS WERE NOT SUCCESSFUL')