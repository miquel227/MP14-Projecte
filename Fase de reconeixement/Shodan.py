import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shodan import Shodan
import socket
from bot import TelegramBot


# Inicialitza el client de Shodan amb la clau API
api_key = 'EA2y81hle78OU28GmrhRJzbEzXZalgXd'
api = Shodan(api_key)

# Defineix la funció per obtenir el nom del servei
def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "Desconegut"

# Demana a l'usuari una direcció IP
ip = input("Introdueix una direcció IP: ")

# Obté la informació de la IP
ip_info = api.host(ip)

# Defineix el nom del fitxer on es guardarà la sortida
output_file = "shodan_resultats.txt"

# Obre el fitxer en mode d'escriptura i guarda la sortida
with open(output_file, "w") as file:
    # Escrivim els noms de domini associats a la IP
    file.write("Noms de domini associats a la IP:\n")
    for domain in ip_info['domains']:
        file.write(domain + "\n")

    # Escrivim els ports oberts trobats per Shodan i els seus noms de servei
    file.write("\nPorts trobats per Shodan:\n")
    for port_info in ip_info['data']:
        port = port_info['port']
        service_name = get_service_name(port)
        file.write(f"Port: {port} - Nom del servei: {service_name}\n")

# Mostra els resultats per terminal
with open(output_file, "r") as file:
    print("Contingut del fitxer:")
    print(file.read())
mi_bot = TelegramBot()
mi_bot.enviar_document(output_file)
os.remove(output_file)