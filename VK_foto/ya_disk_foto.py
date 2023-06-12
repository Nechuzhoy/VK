import os
import requests
from dotenv import load_dotenv

load_dotenv()

class YandexDisk:

    def __init__(self, user_ids, linkToFile, localDestination, ya_token=os.getenv('YA_API_TOKEN')):
        self.ya_token = ya_token
        self.linkToFile = linkToFile
        self.localDestination = localDestination
        self.user_ids = user_ids

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }

    def create_dir(self):
        dir = self.user_ids
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        requests.put(f'{URL}?path={dir}', headers=headers)

    def _get_upload_link(self, disk_file_path):
        self.create_dir()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_foto(self):
        response = requests.get(self.linkToFile)
        with open(self.localDestination, 'wb') as file:
            file.write(response.content)
            return self.localDestination

    def upload_file_to_disk(self):
        filename = self.upload_foto()
        href = self._get_upload_link(f'{self.user_ids}/{os.path.basename(filename)}').get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    ya = YandexDisk(int(input()), 'https:....', r'....')
    ya.upload_file_to_disk()


