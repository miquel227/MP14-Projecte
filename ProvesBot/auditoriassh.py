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
        print("1. Executar una auditoria bàsica.")
        print("2. Executar una auditoria completa.")
        print("3. Tornar al menú principal.")

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
            output_file = os.path.join(current_directory, "AuditoriaCompleta.txt")
            output_text = ssh_audit_all_ports(target)  # Obtenir la sortida
            with open(output_file, "w") as output:
                output.write(output_text)  # Guardar la sortida al fitxer
            print("Contingut del fitxer:")
            print(output_text)  # Mostrar la sortida
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
        os.system('clear' if os.name == 'posix' else 'cls')  # Esborra la pantalla
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