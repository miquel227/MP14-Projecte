import tkinter as tk
from tkinter import ttk
from functools import partial
import subprocess
import os
import socket
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import time
from bot import TelegramBot

class SSHAuditGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SSH Audit GUI")
        self.geometry("500x300")

        self.target_var = tk.StringVar()
        self.output_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="SSH Audit GUI", font=("Helvetica", 16)).pack(pady=10)

        ttk.Label(self, text="Target:").pack(pady=5)
        entry_target = ttk.Entry(self, textvariable=self.target_var)
        entry_target.pack(pady=5)

        ttk.Button(self, text="Scan Specific SSH Server", command=self.scan_specific_ssh).pack(pady=5)
        ttk.Button(self, text="Force IPv4 Scan", command=self.force_ipv4_scan).pack(pady=5)
        ttk.Button(self, text="Debug Scan", command=self.debug_scan).pack(pady=5)
        ttk.Button(self, text="JSON Output Scan", command=self.json_output_scan).pack(pady=5)
        ttk.Button(self, text="Scan All Open SSH Ports", command=self.scan_all_ports).pack(pady=5)

        self.output_label = ttk.Label(self, textvariable=self.output_text)
        self.output_label.pack(pady=10)

    def execute_ssh_audit(self, options):
        target = self.target_var.get()
        current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        output_file = os.path.join(current_directory, "temp_output.txt")

        command = ["ssh-audit"] + options + [target]
        with open(output_file, "w") as output:
            subprocess.run(command, stdout=output)

        with open(output_file, "r") as file:
            output_text = file.read()
            self.output_text.set(output_text)

        mi_bot = TelegramBot()
        mi_bot.enviar_document(output_file)
        os.remove(output_file)

    def ssh_audit_all_ports(self, target):
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

    def scan_specific_ssh(self):
        options = []
        self.execute_ssh_audit(options)

    def force_ipv4_scan(self):
        options = ["-4"]
        self.execute_ssh_audit(options)

    def debug_scan(self):
        options = ["-d"]
        self.execute_ssh_audit(options)

    def json_output_scan(self):
        options = ["-j"]
        self.execute_ssh_audit(options)

    def scan_all_ports(self):
        output_text = self.ssh_audit_all_ports(self.target_var.get())
        self.output_text.set(output_text)
        mi_bot = TelegramBot()
        mi_bot.enviar_document(output_text)

if __name__ == "__main__":
    app = SSHAuditGUI()
    app.mainloop()