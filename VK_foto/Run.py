import VkFoto
import ya_disk_foto
import time
import PySimpleGUI as sg

user_ids = int(input())
foto = VkFoto.VkApiFoto()

if __name__ == '__main__':
    count = []
    for j, i in enumerate(foto.max_size_foto(user_ids)):
        if i[1]['count'] not in count:
            count.append(i[1]['count'])
            disk = ya_disk_foto.YandexDisk(user_ids, f"{i[0]['url']}", f"{i[1]['count']}")
            disk.upload_file_to_disk()

        else:
            disk = ya_disk_foto.YandexDisk(user_ids, f"{i[0]['url']}", f"{i[2]}")
            disk.upload_file_to_disk()

        sg.one_line_progress_meter('Загрузка', j + 1, len(foto.max_size_foto(user_ids)), '-key-')
        time.sleep(1)


