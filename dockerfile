FROM python:3

#Comandes terminal per borrar totes les imatges de docker: docker rmi -f $(docker images -q)
#Comanda terminal per construir la imatge: sudo docker build -t imatge .
#Comanda terminal per executar la imatge: sudo docker run -it imatge

# Actualitza la llista de paquets i instal·la les dependències necessàries
RUN apt-get update && apt-get install -y \
    samba \
    smbclient \
    perl \
    polenum \
    git
RUN apt-get update && apt-get install -y python3-pip ssh-audit nmap

#Instalar shodan i requests
RUN pip3 install requests
RUN pip3 install shodan

# Clona el repositori d'enum4linux des de GitHub
RUN git clone https://github.com/CiscoCXSecurity/enum4linux.git /app/MP14-Projecte/enum4linux

# Instal·la enum4linux i crea els links per a que funcioni
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/enum4linux
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l.pl
RUN ln -s /app/MP14-Projecte/enum4linux/enum4linux.pl /usr/local/bin/e4l-wrapper.sh
RUN ls -l /usr/local/bin/enum4linux

# Copia tot el que hi hagi al directori on esta el dockerfile a la carpeta /app que estara dins del container
# Es important que la carpeta MP14-Projecte estigui dins del directori on esta el dockerfile, que es on esta tot el codi
COPY . /app/

# Defineix la carpeta de treball dins del contenedor de docker
WORKDIR /app/MP14-Projecte

# Comanda per executar el menu que esta dins de la carpeta MP14-Projecte
CMD ["python", "menu.py"]