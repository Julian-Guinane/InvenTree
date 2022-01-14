from json.decoder import JSONDecodeError
import requests


if __name__ == '__main__':
    token = 'eb7fd8221ebfc0184cae53a5ba2a6ca6cc72ec2e'
    headers = {
        'AUTHORIZATION': f'Token {token}'
    }

    print("---------- Barcode Lookup ----------")
    data = {'barcode': '{"part":2}'}
    response = requests.post('http://127.0.0.1:8000/api/barcode/', data=data, headers=headers)
    print(response.json())
    print("------------------------------------")

    if None:
        print("in none")
    else:
        print("not in none")


    print("---------- Autosell Stock ----------")
    data = {
        'action': "autosellstock",
    }
    response = requests.post('http://127.0.0.1:8000/api/action/', data=data, headers=headers)
    try:
        print(response.json())
    except JSONDecodeError:
        print(response)
    print("------------------------------------")












# import coreapi

# token = '9568743a50572d5d7774975d86ac388e8fb5a7ff'

# auth = coreapi.auth.TokenAuthentication(token, scheme='JWT')

# # Initialize a client & load the schema document
# client = coreapi.Client(auth=auth)
# schema = client.get("https://inventory.ammelabs.org/api-doc/")

# # Interact with the API endpoint
# action = ["user", "list"]
# params = {
#     "limit": 3,
#     "offset": 0
# }
# result = client.action(schema, action, params=params)