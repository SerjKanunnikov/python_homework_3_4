from pprint import pprint
from urllib.parse import urlencode
import requests
import config
import json

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
        'user_id': config.MY_ID,
        'fields': 'first_name',
        'access_token': config.TOKEN,
        'v': config.VERSION,
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    # print('?'.join(('https://api.vk.com/method/friends.get', urlencode(params))))
    # print(response.json().get('response').get('items'))
    friend_list = response.json().get('response').get('items')
    friends_of_friends = []
    for person in friend_list:
        params_2 = {
            'user_id': person['id'],
            'fields': 'first_name',
            'access_token': config.TOKEN,
            'v': config.VERSION,
        }
        response_2 = requests.get('https://api.vk.com/method/friends.get', params_2)
        # print(response_2.json().get('response').get('items'))
        friends_of_friends.append(response_2.json())
    # pprint(friend_list)
    my_friends_set = set(friend_list.keys())

    print(my_friends_set)

    # with open("friends_of_friends.txt", "w", encoding="utf-8") as f:
    #     for person in friends_of_friends:
    #         f.write(str(person))
find_my_friends()
