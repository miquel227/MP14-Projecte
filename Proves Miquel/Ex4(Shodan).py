import shodan
import time

# Funció per buscar informació sobre un servei amb límit de resultats i espaiat
def search_service_info(api_key, service_name, max_results=10):
    # Inicialitza el client de Shodan amb la clau API
    api = shodan.Shodan(api_key)

    try:
        # Cerca informació sobre el servei especificat amb el límit de resultats
        results = api.search(f"product:{service_name}", limit=max_results)

        # Mostra els resultats
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']
            print(f"IP: {ip}, Port: {port}")

            # Espaiat de 1 segon entre les sol·licituds per evitar restriccions
            time.sleep(1)

    except shodan.APIError as e:
        print(f'Error: {e}')

# Clau API de Shodan
api_key = 'EA2y81hle78OU28GmrhRJzbEzXZalgXd'

# Demana a l'usuari que introdueixi el nom del servei
service_name = input("Introdueix el nom del servei: ")

# Crida la funció de cerca de servei amb un límit de 10 resultats
search_service_info(api_key, service_name, max_results=1)