from urllib.parse import urlencode
import requests

TOKEN = 'vk1.a.48C6x4ZRe3v2XiUyaVyyPTjcZtR54FeU607YNN0FbY4L48uOK-qrInXZQBnETQa6DJEehX_x8b8SL0DgmuiGsxMagI0Neo5EEV7wU6M5IZ71aUXq4YbthmHa6Ti-8N0ohBF8aNZnTWdsshq1Q5m0QLwTND_4w7MGg2jp_3CzkdwXxrF9y4xBx21P36HM1R8cqQhADtQ_LjH8juj8Lh-jlQ'

APP_ID = '51793204'  #ID моего приложения в VK
OAUTH_BASE_URL = 'https://oauth.vk.com/authorize'
params = {
    'client_id': APP_ID,
    'redirect_url': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'status,photos',
    'response_type': 'token'
}

#oauth_url = f'{OAUTH_BASE_URL}?{urlencode(params)}'
#print(oauth_url)

class VKClient:
    API_BASE_URL = 'https://api.vk.cpm/metod'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.154'
        }

    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(f'{self.API_BASE_URL}/status.get', params=params)
        return response.json()

if __name__ == '__main__':
    vk_client = VKClient(TOKEN, 630379213)
    print(vk_client.get_status())

#    oauth_url = f'{OAUTH_BASE_URL}?{urlencode(params)}'
#    print(oauth_url)