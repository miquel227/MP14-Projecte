import subprocess

ip = input("Introdueix la ip que vols escaneijat amb enum4linux:")
subprocess.run(["enum4linux", "-a", ip])