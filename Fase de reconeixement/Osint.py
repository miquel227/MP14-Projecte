import requests
# Solicitar la direccio IP a l'usuari
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
    else:
        print(f'Error a l\'obtenir informació de geolocalització: {response.status_code}')

except Exception as e:
    print(f'Error: {e}')
