import os
import sys
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import subprocess
from bot import TelegramBot

ip = input("Introdueix la IP que vols escanejar amb enum4linux: ")

# Nom del fitxer on es guardaran els resultats
output_file = "resultats_enum4linux.txt"

print("Procés de l'execució d'enum4linux aquestes tres linies no son un error")
print("Aquest procés tarda uns 30 segons")
try:
    with open(output_file, "w") as output:
        subprocess.run(["/app/MP14-Projecte/enum4linux/enum4linux.pl", "-a", ip], stdout=output)
        time.sleep(1)
except subprocess.CalledProcessError as e:
    print(f"Error al executar enum4linux: {e}")
except FileNotFoundError:
    print("Error: enum4linux no se encuentra en la ruta. ¿Está instalado?")
print("Després de l'execució d'enum4linux")

# Verifiquem si s'ha creat l'arxiu
print("Abans de llegir el contingut de l'arxiu")
with open(output_file, "r") as output:
    content = output.read()
    print("Contingut de l'arxiu:", content)
print("Execcucio del enum4linux finalitzada")

# Enviem i eliminem l'arxiu amb el contingut de l'execucció del programa
if os.path.exists(output_file):
    mi_bot = TelegramBot()
    mi_bot.enviar_document(output_file)
    os.remove(output_file)
