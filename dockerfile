FROM python:3

# Actualitza la llista de paquets i instal·la el mòdul "requests"
RUN apt-get update && apt-get install -y python3-pip ssh-audit nmap
RUN pip3 install requests

# Copia els altres scripts i fitxers
COPY . /app/

# Defineix la carpeta de treball
WORKDIR /app/MP14-Projecte

# Comanda per executar el vostre script principal
CMD ["python", "menu.py"]
