from pprint import pprint
from urllib.parse import urlencode
import requests
import config


# auth_data = {
#     'client_id': config.APP_ID,
#     'redirect_url': 'https://oauth.vk.com/blank.html',
#     'display': 'mobile',
#     'scope': 1026,
#     'response_type': 'token',
#     'v': config.VERSION
# }
#
# print('?'.join((config.URL, urlencode(auth_data))))


def find_my_friends():
    params = {
        'id': '235549',
        'fields': 'first_name',
        'access_token': config.TOKEN,
        'v': config.VERSION,

    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    print('?'.join(('https://api.vk.com/method/friends.get', urlencode(params))))
    print(response.json())
    # response_ids = response.json()
    # for person in ['response']:
    #     print(person)
    # pprint(response_ids)
    # print(type(response_ids))

find_my_friends()
