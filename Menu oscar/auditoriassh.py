import subprocess

def ssh_audit_all_ports(target):
    used_ports = [] #Llista per emmagatzemar els ports en ús
    for port in range(1, 65536):
        result = subprocess.run(["ssh-audit", "-p", str(port), target], capture_output=True, text=True)
        output = result.stdout
        if "SSH server running on" in output:
            print(f"Port {port} is used for SSH.")
            used_ports.append(port)
    if not used_ports:
        print("No SSH servers found on any port.")


def escaneig_Nmap():
    print("Benvingut a l'eina de escaneig Nmap!")
    print("Què vols fer?")
    print("1. Descobrir hosts de xarxa.")
    print("2. Escaneig de ports oberts.")
    print("3. Llistat de serveis i versions.")
    print("4. Llistat de vulnerabilitats.")
    
    opcio = input("Introdueix el número de l'opció que vols: ")

    if opcio == '1':
        subnet = input("Introdueix la subxarxa que vols escanejar (p. ex. 192.168.1.0/24): ")
        subprocess.run(["nmap", "-sn", subnet])
    elif opcio == '2':
        target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
        subprocess.run(["nmap", "-p-", target])
    elif opcio == '3':
        target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
        subprocess.run(["nmap", "-sV", target])
    elif opcio == '4':
        target = input("Introdueix la IP o nom de l'amfitrió que vols escanejar: ")
        subprocess.run(["nmap", "--script", "vuln", target])
    else:
        print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")

def ssh_audit():
    print("Benvingut a l'eina de auditoria SSH!")
    print("Què vols fer amb ssh-audit?")
    print("1. Executar una auditoria bàsica.")
    print("2. Executar una auditoria completa.")
    
    opcio = input("Introdueix el número de l'opció que vols: ")

    if opcio == '1':
        target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
        subprocess.run(["ssh-audit", target])
    elif opcio == '2':
        target = input("Introdueix la IP o nom de l'amfitrió SSH que vols auditar: ")
        ssh_audit_all_ports(target)
    else:
        print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")

if __name__ == "__main__":
    while True:
        print("Quina eina d'auditoria vols utilitzar?")
        print("1. Escaneig Nmap")
        print("2. Auditoria SSH amb ssh-audit")
        print("3. Sortir")
        
        opcio_principal = input("Introdueix el número de l'opció que vols: ")

        if opcio_principal == '1':
            escaneig_Nmap()
        elif opcio_principal == '2':
            ssh_audit()
        elif opcio_principal == '3':
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")
