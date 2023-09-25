from shodan import Shodan

def obtener_servicio_puertos_abiertos(api_key, ip):
    try:
        # Inicializa la instancia de Shodan
        api = Shodan(api_key)

        # Obtiene información del host
        host = api.host(ip)

        servicios = []

        for banner in host['data']:
            puerto = banner['port']
            servicio = banner.get('service', {}).get('name', 'Desconocido')
            servicios.append((puerto, servicio))

        return servicios

    except Exception as e:
        print(f"Error: {str(e)}")
        return []

if __name__ == "__main__":
    api_key = '4Amc7zrhesa5R46pY4tRn1ISrUX0H4hC'

    ip = input("IP: ")

    # Obtener información básica del host
    api = Shodan(api_key)
    host = api.host(ip)

    print("""
            IP: {}
            Organization: {}
            Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    for domains in host['domains']:
        print(domains)
        print(" ")
        print("Puertos Abiertos:")
        for port in host['ports']:
            print("Puerto:" + str(port))

    # Obtener información sobre los servicios en puertos abiertos
    servicios = obtener_servicio_puertos_abiertos(api_key, ip)

    if servicios:
        print("\nServicios en puertos abiertos:")
        for puerto, servicio in servicios:
            print(f"Puerto: {puerto}, Servicio: {servicio}")
    else:
        print("No se encontraron servicios en puertos abiertos.")
