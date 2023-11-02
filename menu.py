import subprocess
import os

def executar_auditoriassh():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/auditoriassh.py'])
    except FileNotFoundError:
        print("L'arxiu auditoriassh.py no s'ha trobat.")
def executar_ennumeracio():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/Ennumeracio.py'])
    except FileNotFoundError:
        print("L'arxiu Ennumeracio.py no s'ha trobat.")
def executar_escaneig_nmap():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/escaneignmap.py'])
    except FileNotFoundError:
        print("L'arxiu escaneig_nmap.py no s'ha trobat.")
def executar_harvester():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Harvester.py'])
    except FileNotFoundError:
        print("L'arxiu Harvester.py no s'ha trobat.")
def executar_osint():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/osint.py'])
    except FileNotFoundError:
        print("L'arxiu osint.py no s'ha trobat.")
def executar_shodan():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Shodan.py'])
    except FileNotFoundError:
        print("L'arxiu Shodan.py no s'ha trobat.")

def menu():
    while True:
        print("Menú:")
        print("1. Executar Auditoria SSH")
        print("2. Executar Ennumeració")
        print("3. Executar Escaneig Nmap")
        print("4. Executar Harvester")
        print("5. Executar OSINT")
        print("6. Executar Shodan")
        print("7. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_auditoriassh()
        elif opcio == "2":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_ennumeracio()
        elif opcio == "3":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_escaneig_nmap()
        elif opcio == "4":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_harvester()
        elif opcio == "5":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_osint()
        elif opcio == "6":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_shodan()
        elif opcio == "7":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")
            
if __name__ == "__main__":
    menu()