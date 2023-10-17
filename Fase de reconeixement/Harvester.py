#import subprocess
#objectiu = input("Introduïu l'objectiu (domini, correu electrònic, etc.): ")
#opcions = input("Introduïu les opcions de The Harvester (p. ex., -d per domini): ")

#comanda = f"theharvester -d {objectiu} {opcions}"
#subprocess.call(comanda, shell=True)

import subprocess

objectiu = input("Introduïu l'objectiu (domini, correu electrònic, etc.): ")
opcions = input("Introduïu les opcions de The Harvester (p. ex., -l 5 -b bing): ")

# Utilizamos la ruta completa al script theHarvester.py
comanda = f"python3.10 /home/alumne/theHarv/theHarvester/theHarvester.py -d {objectiu} {opcions}"

# Intentamos ejecutar la comanda
try:
    subprocess.run(comanda, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar The Harvester: {e}")
except FileNotFoundError:
    print("Error: The Harvester no se encuentra en la ruta. ¿Está instalado?")