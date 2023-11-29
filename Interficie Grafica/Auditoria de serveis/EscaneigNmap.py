import tkinter as tk
from tkinter import ttk
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot
import subprocess


class NmapScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Eina d'Escaneig Nmap")

        # Configuración del tamaño de la ventana
        window_width = 600
        window_height = 400

        # Configuración de la posición de la ventana en el centro
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Què vols fer?").pack(pady=10)

        options = ["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions",
                   "Llistat de vulnerabilitats", "Tornar al menú principal"]

        self.option_var = tk.StringVar()
        self.option_var.set(options[0])

        option_menu = ttk.Combobox(self.root, textvariable=self.option_var, values=options)
        option_menu.pack(pady=10)

        entry_label = ttk.Label(self.root, text="Introdueix la IP o nom de l'amfitrió:")
        entry_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.entry_var)
        entry.pack(pady=10)

        ttk.Button(self.root, text="Executar", command=self.execute_option).pack(pady=10)

        # Configurar la tecla "Enter" para que ejecute la opción
        self.root.bind('<Return>', lambda event=None: self.execute_option())

    def execute_option(self):
        selected_option = self.option_var.get()
        entry_value = self.entry_var.get()

        if selected_option == "Descobrir hosts de xarxa":
            self.discover_network_hosts()
        elif selected_option == "Escaneig de ports oberts":
            self.scan_open_ports(entry_value)
        elif selected_option == "Llistat de serveis i versions":
            self.list_services_and_versions(entry_value)
        elif selected_option == "Llistat de vulnerabilitats":
            self.list_vulnerabilities(entry_value)
        elif selected_option == "Tornar al menú principal":
            self.root.destroy()

    def discover_network_hosts(self):
        subnet = self.get_input("Introdueix la subxarxa que vols escanejar (p. ex. 192.168.1.0/24): ")
        output_file = "HostsDeLaXarxa.txt"
        self.run_nmap(["nmap", "-sn", subnet], output_file)

    def scan_open_ports(self, target):
        output_file = "PortsOberts.txt"
        self.run_nmap(["nmap", "-p-", target], output_file)

    def list_services_and_versions(self, target):
        output_file = "Serveis&Versions.txt"
        self.run_nmap(["nmap", "-sV", target], output_file)

    def list_vulnerabilities(self, target):
        print("Aquest procés pot trigar més de 70 segons.")
        output_file = "Vulnerabilitats.txt"
        self.run_nmap(["nmap", "--script", "vuln", target], output_file)

    def run_nmap(self, command, output_file):
        current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        output_file = os.path.join(current_directory, output_file)

        with open(output_file, "w") as output:
            subprocess.run(command, stdout=output)

        self.display_result(output_file)
        mi_bot = TelegramBot()
        mi_bot.enviar_document(output_file)
        os.remove(output_file)

    def display_result(self, output_file):
        with open(output_file, "r") as file:
            result_text = file.read()
            result_window = tk.Toplevel(self.root)
            result_window.title("Resultats")
            result_label = ttk.Label(result_window, text=result_text)
            result_label.pack()

    def get_input(self, prompt):
        input_window = tk.Toplevel(self.root)
        input_window.title("Introduir dades")
        input_label = ttk.Label(input_window, text=prompt)
        input_label.pack()
        entry_var = tk.StringVar()
        entry = ttk.Entry(input_window, textvariable=entry_var)
        entry.pack()
        entry.focus_set()
        ok_button = ttk.Button(input_window, text="OK", command=lambda: input_window.destroy())
        ok_button.pack()
        input_window.wait_window()
        return entry_var.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = NmapScannerGUI(root)
    root.mainloop()