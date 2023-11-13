import requests

# Solicitar la dirección IP al usuario
ip_address = input("Introduce la dirección IP que deseas geolocalizar: ")

# URL de la API de ipinfo.io
api_url = f'https://ipinfo.io/{ip_address}/json'

try:
    # Realizar una solicitud GET a la API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Extraer la información de geolocalización
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
        print(f'Error al obtener información de geolocalización: {response.status_code}')

except Exception as e:
    print(f'Error: {e}')