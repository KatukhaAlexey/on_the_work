import requests
from pprint import pprint
import os


with open('vk_token_id.txt', 'r') as f:
    vk_token = f.readline().strip()
    vk_user_id = f.readline().strip()


class vk_api_client:
    api_base_url = 'https://api.vk.com/method/'

    def __init__(self, vk_token, vk_user_id):
        self.vk_token = vk_token
        self.vk_user_id = vk_user_id
    def get_params(self):
        return {
            'access_token': self.vk_token,
            'v': '5.131'
        }

    def _build_url(self, api_method):
        return f'{self.api_base_url}/{api_method}'


    def get_photos(self):
        params = self.get_params()
        params.update({'owner_id': self.vk_user_id, 'album_id': 'profile'})
        response = requests.get(self._build_url('photos.get'), params=params)
        response = response.json()


        return response


if __name__ == '__main__':

    vk_client = vk_api_client(vk_token, vk_user_id)

    pprint(vk_client.get_photos(), sort_dicts=False, width=100)