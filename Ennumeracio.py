import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import subprocess
from bot import TelegramBot

ip = input("Introdueix la ip que vols escanejar amb enum4linux: ")

# Nombre del archivo de salida
output_file = "resultats_enum4linux.txt"

# Intentamos ejecutar enum4linux y guardar la salida en el archivo
try:
    with open(output_file, "w") as output:
        subprocess.run(["enum4linux", "-a", ip], stdout=output)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar enum4linux: {e}")
except FileNotFoundError:
    print("Error: enum4linux no se encuentra en la ruta. ¿Está instalado?")

# Verificar si se ha creado el archivo y enviarlo al bot de Telegram
if os.path.exists(output_file):
    mi_bot = TelegramBot()
    mi_bot.enviar_document(output_file)
    os.remove(output_file)