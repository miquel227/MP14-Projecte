import subprocess

def ejecutar_shodan():
    try:
        # Ejecutar shodan.py desde la carpeta Shodan usando una ruta relativa
        subprocess.run(['python3', 'Fase de reconeixement/Shodan.py'])
    except FileNotFoundError:
        print("El archivo Shodan.py no se encontró.")

def ejecutar_nmap():
    try:
        # Ejecutar shodan.py desde la carpeta Shodan usando una ruta relativa
        subprocess.run(['python3', 'Auditoria de serveis/escaneignmap.py'])
    except FileNotFoundError:
        print("El archivo Shodan.py no se encontró.")


def menu():
    while True:
        print("1. Ejecutar Shodan")
        print("2. Otra opción")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_shodan()
        elif opcion == "2":
            ejecutar_nmap()
            pass
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
