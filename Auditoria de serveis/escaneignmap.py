import subprocess
import os

def escaneig_Nmap():
    while True:
        print("Benvingut a l'eina de escaneig Nmap!")
        print("Què vols fer?")
        print("1. Descobrir hosts de xarxa.")
        print("2. Escaneig de ports oberts.")
        print("3. Llistat de serveis i versions.")
        print("4. Llistat de vulnerabilitats.")
        print("5. Sortir")
        
        opcio = input("Introdueix el número de l'opció que vols: ")

        if opcio == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            subnet = input("Introdueix la subxarxa que vols escanejar (p. ex. 192.168.1.0/24): ")
            subprocess.run(["nmap", "-sn", subnet])
        elif opcio == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
            subprocess.run(["nmap", "-p-", target])
        elif opcio == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
            subprocess.run(["nmap", "-sV", target])
        elif opcio == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
            subprocess.run(["nmap", "--script", "vuln", target])
        elif opcio == '5':
            print("Tornant al menú principal.")
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")

if __name__ == "__main__":
    escaneig_Nmap()
