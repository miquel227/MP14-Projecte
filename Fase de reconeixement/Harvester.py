import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot import TelegramBot 
import subprocess

objectiu = input("Introduïu l'objectiu (p. ex: iesebre.com -l 200 -b yahoo): ")

# Utilizamos la ruta completa al script theHarvester.py
comanda = f"python3 /app/MP14-Projecte/theHarvester/theHarvester.py -d {objectiu}"

# Nome del fitxer on es guardaran els resultats
output_file = "Harvester_resultats.txt"

# Executem la comanda i guardem el resultat en un fitxer
try:
    with open(output_file, "w") as output:
        subprocess.run(comanda, shell=True, check=True, stdout=output)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar The Harvester: {e}")
except FileNotFoundError:
    print("Error: The Harvester no se encuentra en la ruta. ¿Está instalado?")

# Enviem el fitxer amb el resultat de l'execució del programa
if os.path.exists(output_file):
    mi_bot = TelegramBot()
    mi_bot.enviar_document(output_file)
    os.remove(output_file)
else:
    print("No se ha generado el archivo de resultados.")