from shodan import Shodan
import socket

#API Key
api_key = 'EA2y81hle78OU28GmrhRJzbEzXZalgXd'

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "Desconegut"

api = Shodan(api_key)
    
# Solicita al usuari una direcció IP
ip = input("Introueix una direcció IP: ")

# Obteneix la informació de la IP
ip_info = api.host(ip)

# Mostra els noms de domini asociats a la IP
print("Noms de domini asociats a la IP:")
for domain in ip_info['domains']:
    print(domain)

# Mostra els ports oberts trobats per Shodan y els seus noms de servei
print("\nPorts trobats per Shodan:")
for port_info in ip_info['data']:
    port = port_info['port']
    service_name = get_service_name(port)
    print(f"Port: {port} - Nom del servei: {service_name}")

# Afegeix una funció on l'usuari pugui escriure el nom d'un servei (per exemple proftp) i es mostri un resultats amb ips i ports on s'hi pugui trobar aquest servei segons els resultats de Shodan.
