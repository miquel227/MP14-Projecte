import requests

class TelegramBot:
    def __init__(self):
        self.token = '6889677932:AAHlD9wD_ErIn7rD8nvlHGC7-7eKY8NzHEE'
        self.chat_id = '-1002143597676'
    
    def enviar_mensaje(self, mensaje):
        response = requests.post(
            'https://api.telegram.org/bot' + self.token + '/sendMessage',
            data={'chat_id': self.chat_id, 'text': mensaje, 'parse_mode': 'HTML'}
        )
        if response.status_code == 200:
            print('El missatge s\'ha enviat correctament.')
        else:
            print('El missatge no s\'ha pogut enviar.')
    
    def enviar_document(self, document_path):
        with open(document_path, 'rb') as doc_file:
            response = requests.post(
                'https://api.telegram.org/bot' + self.token + '/sendDocument',
                data={'chat_id': self.chat_id},
                files={'document': doc_file}
            )
            if response.status_code == 200:
                print('El document amb els resultats s\'ha enviat correctament.')
            else:
                print('El document amb els resultats no s\'ha pogut enviar.')

    def mensaje(self, text):
        self.enviar_mensaje(text)

mi_bot = TelegramBot()
