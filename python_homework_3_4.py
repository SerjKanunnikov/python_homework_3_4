from pprint import pprint
from urllib.parse import urlencode
import requests
import config

# Авторизация
#
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
    """Поиск моих друзей и формирование множества с идентификаторами"""
    params = {
        'user_id': config.MY_ID,
        'fields': 'first_name',
        'access_token': config.TOKEN,
        'v': config.VERSION,
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friend_list = response.json().get('response').get('items')
    friend_ids = []
    for person in friend_list:
        friend_ids.append(person["id"])
    set_of_my_friends = set(friend_ids)
    return set_of_my_friends


def find_friends_of_my_friends(set_of_my_friends):
    """Поиск друзей друзей формирование множества с идентификаторами"""
    friends_of_my_friends_list = []
    for user_id in set_of_my_friends:
        params = {
            'user_id': user_id,
            'fields': 'first_name',
            'access_token': config.TOKEN,
            'v': config.VERSION,
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        friends_of_my_friends_list.append(response.json().get('response').get('items'))
    friends_of_my_friends_ids = []
    for sublist in friends_of_my_friends_list:
        for person in sublist:
            friends_of_my_friends_ids.append(person["id"])
    set_of_friends_of_my_friends = set(friends_of_my_friends_ids)
    return set_of_friends_of_my_friends


def intersection(set_of_my_friends, set_of_friends_of_my_friends):
    """Поиск пересечений множеств друзей и друзей друзей"""
    common_friends_ids = set_of_my_friends & set_of_friends_of_my_friends
    return common_friends_ids


def output(common_friends_ids):
    """Вывод друзей, с которыми есть общие друзья"""
    params = {
        'user_ids': str(common_friends_ids),
        'fields': 'first_name',
        'access_token': config.TOKEN,
        'v': config.VERSION,
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    common_friends = response.json().get('response')
    print("Друзья, с которыми есть общие друзья: ")
    for person in common_friends:
            print(person["first_name"], person["last_name"])

if __name__ == "__main__":
    output(intersection(find_my_friends(), find_friends_of_my_friends(find_my_friends())))
