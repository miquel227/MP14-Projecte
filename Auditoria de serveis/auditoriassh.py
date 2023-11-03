import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot
import subprocess
import socket
import os

def ssh_audit_all_ports(target):
    used_ports = []  # Llista per emmagatzemar els ports en ús

    # Escanejar tots els ports SSH en el rang 1-65535
    for port in range(1, 65536):
        # Verificar si el port està en ús
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Temps d'espera per a la connexió (1 segon)
        resultat = sock.connect_ex((target, port))
        sock.close()

        if resultat == 0:
            used_ports.append(port)

    if not used_ports:
        return "No s'ha trobat cap servidor SSH en cap port."
    
    return "\n".join([f"Port {port} és utilitzat per SSH." for port in used_ports])

def ssh_audit():
    while True:
        print("Benvingut a l'eina d'auditoria SSH!")
        print("Què vols fer amb ssh-audit?")
        print("1. Escanejar un servidor SSH específic")
        print("2. Escaneig forçant ipv4")
        print("3. Escaneig amb depuració (debug) ")
        print("4. Mostrar la sortida en format JSON")
        print("5. Escaneijar tots el ports SSH obersts")
        print("6. Tornar al menú principal.")

        opcio = input("Introdueix el número de l'opció que vols: ")

        if opcio == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaBàsica.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaForçantIPv4.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-4", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaPortDiferent.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-d", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaJSON.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-j", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '5':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "PortsSSH_Oberts.txt")
            output_text = ssh_audit_all_ports(target)  
            with open(output_file, "w") as output:
                output.write(output_text)  
            print("Contingut del fitxer:")
            print(output_text)  
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
        elif opcio == '3':
            print("Tornant al menú principal.")
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")

if __name__ == "__main__":
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Quina eina d'auditoria vols utilitzar?")
        print("1. Auditoria SSH amb ssh-audit")
        print("2. Sortir")
        
        opcio_principal = input("Introdueix el número de l'opció que vols: ")

        if opcio_principal == '1':
            ssh_audit()
        elif opcio_principal == '2':
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")