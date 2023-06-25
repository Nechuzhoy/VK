import VkFoto
import ya_disk_foto
import time
import PySimpleGUI as sg
import json

ya_token = input("Яндекс диск токен: ")
user_ids = int(input("Введите id юзера: "))
folder_name = input("Введите название папки для загрузки фото: ")
foto = VkFoto.VkApiFoto()
print(f'Для скачивания доступно {len(foto.max_size_foto(user_ids))} фото')
count_foto = int(input('Сколько фото скачать? : '))
if __name__ == '__main__':
    count = []
    list_foto = []
    for j, i in enumerate(foto.max_size_foto(user_ids)):
        if i[1]['count'] not in count:
            count.append(i[1]['count'])
            disk = ya_disk_foto.YandexDisk(user_ids, folder_name, f"{i[0]['url']}", f"{i[1]['count']}.jpg", ya_token)
            disk.upload_file_to_disk()


            if j + 1 == count_foto:
                break
        else:
            disk = ya_disk_foto.YandexDisk(user_ids, folder_name, f"{i[0]['url']}", f"{i[2]}.jpg", ya_token)
            disk.upload_file_to_disk()
        list_foto.append(i)
        sg.one_line_progress_meter('Загрузка', j + 1, len(foto.max_size_foto(user_ids)), '-key-')
        time.sleep(1)

        file = f'{user_ids}.json'
        with open(file, 'w') as f:
            json.dump(list_foto, f)
