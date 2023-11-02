import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot 
import subprocess

objectiu = input("Introduïu l'objectiu (domini, correu electrònic, etc.): ")
opcions = input("Introduïu les opcions de The Harvester (p. ex., -l 5 -b bing): ")

# Utilizamos la ruta completa al script theHarvester.py
comanda = f"python3.10 /home/alumne/theHarv/theHarvester/theHarvester.py -d {objectiu} {opcions}"

# Nombre del archivo de salida
output_file = "Harvester_resultats.txt"

# Intentamos ejecutar la comanda y guardar la salida en el archivo
try:
    with open(output_file, "w") as output:
        subprocess.run(comanda, shell=True, check=True, stdout=output)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar The Harvester: {e}")
except FileNotFoundError:
    print("Error: The Harvester no se encuentra en la ruta. ¿Está instalado?")

# Verificar si se ha creado el archivo y enviarlo al bot de Telegram
if os.path.exists(output_file):
    mi_bot = TelegramBot()
    mi_bot.enviar_document(output_file)
    os.remove(output_file)
else:
    print("No se ha generado el archivo de resultados.")