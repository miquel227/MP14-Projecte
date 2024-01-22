from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

def executar_auditoriassh():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/auditoriassh.py'])
    except FileNotFoundError:
        return "L'arxiu auditoriassh.py no s'ha trobat."

def executar_ennumeracio():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/Ennumeracio.py'])
    except FileNotFoundError:
        return "L'arxiu Ennumeracio.py no s'ha trobat."

def executar_escaneig_nmap():
    try:
        subprocess.run(['python3', 'Auditoria de serveis/escaneignmap.py'])
    except FileNotFoundError:
        return "L'arxiu escaneig_nmap.py no s'ha trobat."

def executar_harvester():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Harvester.py'])
    except FileNotFoundError:
        return "L'arxiu Harvester.py no s'ha trobat."

def executar_osint():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Osint.py'])
    except FileNotFoundError:
        return "L'arxiu osint.py no s'ha trobat."

def executar_shodan():
    try:
        subprocess.run(['python3', 'Fase de reconeixement/Shodan.py'])
    except FileNotFoundError:
        return "L'arxiu Shodan.py no s'ha trobat."

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/execute', methods=['POST', 'GET'])
def execute():
    option = request.form['option']
    result_text = ""

    if option == '1':
        result_text = executar_auditoriassh()
    elif option == '2':
        result_text = executar_ennumeracio()
    elif option == '3':
        result_text = executar_escaneig_nmap()
    elif option == '4':
        result_text = executar_harvester()
    elif option == '5':
        result_text = executar_osint()
    elif option == '6':
        result_text = executar_shodan()
    elif option == '7':
        try:
            subprocess.run(['python3', 'Interficie Grafica/Interficie.py'])
        except FileNotFoundError:
            result_text = "L'arxiu Interficie.py no s'ha trobat."

    return render_template('result.html', result=result_text)


if __name__ == "__main__":
    app.run(debug=True)
