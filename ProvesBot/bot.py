 #!/usr/bin/env python3
import requests

class TelegramBot:
    def __init__(self):
        self.token = '5761203078:AAEmSQL6Ll1IZX4RHqO6K7eVS8QbYFNk2wg'
        self.chat_id = '-1002084646469'
    
    def enviar_mensaje(self, mensaje):
        response = requests.post(
            'https://api.telegram.org/bot' + self.token + '/sendMessage',
            data={'chat_id': self.chat_id, 'text': mensaje, 'parse_mode': 'HTML'}
        )
        if response.status_code == 200:
                print('El missatge sha enviat correctament.')
        else:
            print('El missatge no sha pogut enviar.')
    def mensaje(self, text):
         self.enviar_mensaje(text)


def funcion_remota():
    print("Executant funció remota.")


mi_bot = TelegramBot()