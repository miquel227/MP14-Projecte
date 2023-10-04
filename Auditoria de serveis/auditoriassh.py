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
            print(f"Port {port} és utilitzat per SSH.")
            used_ports.append(port)

    if not used_ports:
        print("No s'ha trobat cap servidor SSH en cap port.")

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
            subprocess.run(["ssh-audit", target])
        elif opcio == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
            ssh_audit_all_ports(target)
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
