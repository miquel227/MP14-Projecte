from bot import TelegramBot  # Assegura't que la importació del teu mòdul sigui correcta
import subprocess
import socket

def ssh_audit_all_ports(target):
    used_ports = []
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            used_ports.append(port)

    if not used_ports:
        return "No s'ha trobat cap servidor SSH en cap port."
    
    return "\n".join([f"Port {port} és utilitzat per SSH." for port in used_ports])

if __name__ == "__main__":
    target = sys.argv[1]
    output_file = sys.argv[2]
    option = sys.argv[3]

    if option == '3':
        subprocess.run(["ssh-audit", target], stdout=open(output_file, 'w'))
    elif option == '4':
        subprocess.run(["ssh-audit", "-4", target], stdout=open(output_file, 'w'))
    elif option == '5':
        subprocess.run(["ssh-audit", "-d", target], stdout=open(output_file, 'w'))
    elif option == '6':
        subprocess.run(["ssh-audit", "-j", target], stdout=open(output_file, 'w'))
    elif option == '7':
        output_text = ssh_audit_all_ports(target)
        with open(output_file, 'w') as output:
            output.write(output_text)

    mi_bot = TelegramBot()
    mi_bot.enviar_document(output_file)
