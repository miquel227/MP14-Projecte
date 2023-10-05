import subprocess
objectiu = input("Introduïu l'objectiu (domini, correu electrònic, etc.): ")
opcions = input("Introduïu les opcions de The Harvester (p. ex., -d per domini): ")

comanda = f"theharvester -d {objectiu} {opcions}"
subprocess.call(comanda, shell=True)