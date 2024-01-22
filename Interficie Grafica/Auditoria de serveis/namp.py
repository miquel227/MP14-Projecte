from flask import Flask, render_template, request, send_file, redirect
import os
print("Ruta de treball actual:", os.getcwd())
app = Flask(__name__)
app.template_folder = os.path.abspath(os.path.dirname(__file__))
import subprocess
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from bot import TelegramBot  # Assegura't que la importació del teu mòdul sigui correcta
import time

app = Flask(__name__)

def executar_nmap(option, target):
    output_file = ''

    if option == '1':
        output_file = "HostsDeLaXarxa.txt"
        cmd = ["nmap", "-sn", target, "-oN", output_file]
    elif option == '2':
        output_file = "PortsOberts.txt"
        cmd = ["nmap", "-p-", target, "-oN", output_file]
    elif option == '3':
        output_file = "ServeisVersions.txt"
        cmd = ["nmap", "-sV", target, "-oN", output_file]
    elif option == '4':
        output_file = "Vulnerabilitats.txt"
        cmd = ["nmap", "--script", "vuln", target, "-oN", output_file]
    else:
        return "Opció no vàlida"

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Espera que la comanda finalitzi i recull la sortida
    output, error = process.communicate()

    if process.returncode == 0:
        result_text = f"Escaneig completat amb èxit:\n{output}"
    else:
        result_text = f"Error en l'escaneig:\n{error}"

    return result_text


if __name__ == "__main__":
    app.run(debug=True)