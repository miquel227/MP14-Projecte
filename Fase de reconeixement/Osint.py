import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot 
import os
import requests

# Solicitar la direcció IP a l'usuari
ip_address = input("Introdueix la IP que vols geolocalitzar: ")

# URL de la API de ipinfo.io
api_url = f'https://ipinfo.io/{ip_address}/json'

try:
    # Realitzar una solicitud GET a la API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Extraure la informació de geolocalització
        ip = data['ip']
        city = data['city']
        region = data['region']
        country = data['country']
        location = data['loc']

        print(f'IP: {ip}')
        print(f'City: {city}')
        print(f'Region: {region}')
        print(f'Country: {country}')
        print(f'Location: {location}')

        # Crear un nom de fitxer únic basat en la IP
        output_file = f"geolocalitzacio_{ip_address}.txt"

        # Crear el contingut del fitxer amb la informació de geolocalització
        file_content = f"""
        IP: {ip}
        City: {city}
        Region: {region}
        Country: {country}
        Location: {location}
        """

        # Guardar el contingut en el fitxer
        with open(output_file, "w") as output:
            output.write(file_content)

        # Verificar si el fitxer s'ha creat i enviar-lo al bot de Telegram
        if os.path.exists(output_file):
            mi_bot = TelegramBot()

            # Utilitza el mètode apropiat del teu bot per a enviar fitxers
            mi_bot.enviar_document(output_file)

            # Eliminar el fitxer després d'enviar-lo
            os.remove(output_file)

            print("Fitxer enviat correctament al bot de Telegram.")
        else:
            print("No s'ha generat el fitxer de resultats.")
    else:
        print(f'Error a l\'obtenir informació de geolocalització: {response.status_code}')

except Exception as e:
    print(f'Error: {e}')
