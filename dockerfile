# Usa una imatge base de Python 3
FROM python:3

#Com crear la imatge a partir del Dockerfile: docker build -t mp14-projecte .   
#Com executar la imatge: docker run -it mp14-projecte

# Actualitza la llista de paquets i instal·la les dependències necessàries
RUN apt-get update && apt-get install -y \
    samba \
    smbclient \
    perl \
    polenum \
    git
RUN apt-get update && apt-get install -y python3-pip ssh-audit nmap

# Instal·la les dependencies de Python per a The Harvester
RUN pip3 install requests

# Clona el repositori d'enum4linux des de GitHub
RUN git clone https://github.com/CiscoCXSecurity/enum4linux.git /app/MP14-Projecte/enum4linux

# Instal·la enum4linux i crea els enllaços perquè funcioni
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/enum4linux
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l.pl
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l-wrapper.sh
RUN ls -l /usr/local/bin/enum4linux

# Copia tot el que hi hagi al directori on està el Dockerfile a la carpeta /app que estarà dins del container
# És important que la carpeta MP14-Projecte estigui dins del directori on està el Dockerfile, que és on està tot el codi
COPY . /app/

# Defineix la carpeta de treball dins del contenidor de Docker
WORKDIR /app/MP14-Projecte

# Comanda per instal·lar The Harvester i altres dependències
RUN git clone https://github.com/laramies/theHarvester.git && \
    cd theHarvester && \
    pip3 install -r requirements.txt && \
    chmod +x theHarvester.py && \
    ln -s /app/MP14-Projecte/theHarvester/theHarvester.py /usr/local/bin/theHarvester

# Comanda per executar el menu que està dins de la carpeta MP14-Projecte
CMD ["python", "menu.py"]