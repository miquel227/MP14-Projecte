import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot
import subprocess
import time

def escaneig_Nmap():
    while True:
        print("Benvingut a l'eina de escaneig Nmap!")
        print("Què vols fer?")
        print("1. Descobrir hosts de xarxa.")
        print("2. Escaneig de ports oberts.")
        print("3. Llistat de serveis i versions.")
        print("4. Llistat de vulnerabilitats.")
        print("5. Tornanr al menú principal.")
        
        opcio = input("Introdueix el número de l'opció que vols: ")

        if opcio == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            subnet = input("Introdueix la subxarxa que vols escanejar (p. ex. 192.168.1.0/24): ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "HostsDeLaXarxa.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "-sn", subnet], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "PortsOberts.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "-p-", target], stdout=output)
                with open(output_file, "r") as file:
                    print("Contingut del fitxer:")
                    print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "Serveis&Versions.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "-sV", target], stdout=output)
                with open(output_file, "r") as file:
                    print("Contingut del fitxer:")
                    print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
            print("Aquest procés pot trigar mes de 70 segons.")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "Vulnerabilitats.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "--script", "vuln", target], stdout=output)
                with open(output_file, "r") as file:
                    print("Contingut del fitxer:")
                    print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '5':
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Tornant al menú principal....")
            time.sleep(1.5)
            os.system('clear' if os.name == 'posix' else 'cls')
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")

if __name__ == "__main__":
    escaneig_Nmap()
