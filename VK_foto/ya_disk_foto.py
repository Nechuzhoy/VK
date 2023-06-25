import os
import requests
from dotenv import load_dotenv
import Status_Http
load_dotenv()
cod = Status_Http.Status_Cod()
class YandexDisk:

    def __init__(self, user_ids, folder_name, linkToFile, localDestination, ya_token):
        self.ya_token = ya_token
        self.linkToFile = linkToFile
        self.localDestination = localDestination
        self.user_ids = user_ids
        self.folder_name = folder_name

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }

    def create_dir(self):
        dir = self.folder_name
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        response = requests.put(f'{URL}?path={dir}', headers=headers)
        print(f'Создание папки на Яндекс Диске: {cod.server_cod(response)}')


    def _get_upload_link(self, disk_file_path):
        self.create_dir()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(f'Запрос - 2: {cod.server_cod(response)}')
        return response.json()

    def upload_foto(self):
        response = requests.get(self.linkToFile)
        print(f'Запрос - 1: {cod.server_cod(response)}')
        with open(self.localDestination, 'wb') as file:
            file.write(response.content)
            return self.localDestination

    def upload_file_to_disk(self):
        filename = self.upload_foto()
        href = self._get_upload_link(f'{self.folder_name}/{os.path.basename(filename)}').get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        print(f'Запрос - 3: {cod.server_cod(response)}')





