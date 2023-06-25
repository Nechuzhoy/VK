class Status_Cod():
    def __int__(self, response):
        self.response = response

    def server_cod(self, response):
        if response.status_code <= 400:
            return "Успех"
        else:
            return f'Ошибка, код ответа {response.status_code}'

