import os
import requests
from dotenv import load_dotenv
from operator import itemgetter
from pprint import pprint

load_dotenv()


class VkApiFoto:

    def __init__(self, vk_token=os.getenv('VK_API_TOKEN'),
                 version=os.getenv('VERSION')):
        self.params = {
            'access_token': vk_token,
            'v': version
        }

    def get_user_foto(self, user_ids, field=1):
        metod_name = 'https://api.vk.com/method/photos.getAll'
        params = {'owner_id': user_ids, 'extended': field,
                  **self.params}
        response = requests.get(metod_name, params=params)
        return response.json()

    def sort_foto(self, user_ids):
        list_foto = self.get_user_foto(user_ids)
        return [[i['sizes'], i['likes'], i['date']] for i in list_foto['response']['items']]

    def max_size_foto(self, user_ids):
        list_size_foto = self.sort_foto(user_ids)
        list_max_size_foto = []
        for foto in list_size_foto:
            list_max_size_foto.append(
                [max(foto[0], key=itemgetter('width')), foto[1], (time.ctime(int(foto[2])).replace(":", ""))])
        return list_max_size_foto


if __name__ == '__main__':
    vk = VkApiFoto()
    pprint(vk.max_size_foto(int(input())))
