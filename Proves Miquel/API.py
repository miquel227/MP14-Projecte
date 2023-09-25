## Realitza un petit programa que pregunti una ip a l'usuari i mostri la informació d'aquesta IP rebuda des de l'API de shodan.

import test
import os


def main():
    # API key
    API_KEY = os.environ.get('SHODAN_API_KEY')
    api = test.Shodan(API_KEY)

    # Ask the user for input
    ip = input("IP: ")

    # Lookup the host
    host = api.host(ip)

    # Print general info
    print("""
            IP: {}
            Organization: {}
            Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    # Print all banners
    for item in host['data']:
        print("""
                Port: {}
                Banner: {}
        """.format(item['port'], item['data']))