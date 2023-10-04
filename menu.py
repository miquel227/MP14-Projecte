import subprocess
import os

def executar_shodan():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Shodan.py'])
    except FileNotFoundError:
        print("L'arxiu Shodan.py no s'ha trobat.")

def executar_nmap():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/escaneignmap.py'])
    except FileNotFoundError:
        print("L'arxiu escaneig_nmap.py no s'ha trobat.")

def menu():
    while True:
        print("Menú:")
        print("1. Executar Shodan")
        print("2. Executar Nmap")
        print("3. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_shodan()
        elif opcio == "2":
            os.system('clear' if os.name == 'posix' else 'cls')
            executar_nmap()
        elif opcio == "3":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    menu()