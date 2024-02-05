# Guia Usuari

###**Requeriments per poder utilitzar el nostre programari.**

+ Qualsevol Sistema Operatiu de Linux

+ <p>Docker Compose instal·lat (mira <a href="https://docs.docker.com/engine/install/" title="Title">Instalar Docker Compose)</a></p>

+ Potser també una tasa de café o de té :)

###**Primer Pas: Descarregar l'última versió del nostre codi**

```
docker pull miqueldieguez123/mp14-projecte
docker run -it miqueldieguez123/mp14-projecte
```

-------------------------------------------------------------------------
###**Segon Pas: Començem amb la execució del programa**
Per començar, al executar el nostre programari d'auditoria podem veure que ens surten una sèrie d'opcions:

Com veiem, aquestes són les opcions d'auditoria del programa.
En aquesta guia explicarem per ordre de números les següents opcions que hi han. 

![Descripción de la imagen](/Imatges/1.jpeg)

Seleccionant l'opció 1 "Executar Auditoria SSH" entrarem a un submenú.

![Descripción de la imagen](/Imatges/2.jpeg)

En aquest submenú tindrem una varietat d'opcions d'escaneig amb l'eina ssh-audit, no obstant això encara que cada vegada que entressiu a cada opció i hi hagi la mateixa sortida, cadascuna fà un escaneig diferent que us explicarem a continuació j.

![Descripción de la imagen](/Imatges/3.png)

La sortida següent és la que us sortirà per a **CADA** opció del primer submenú.

![Descripción de la imagen](/Imatges/4.png)

####**Opció 1 (Escanejar un servidor SSH específic):**

Aquesta opció fà que l'eina realitzi un escaneig de la IP objectiu amb aquesta direcció (normalment s'utilitza per a servidors SSH) i presenta un informe detallat sobre la configuració de seguretat del servidor.

Aquest informe pot incloure informació sobre les versions del protocol SSH admeses, algoritmes de xifrat utilitzats, configuracions de claus i altres configuracions de seguretat relacionades amb SSH. La sortida proporcionada per ssh-audit t'ajuda a avaluar la robustesa de la configuració de seguretat de la IP objectiu i a prendre mesures per reforçar-la si és necessari.

Exemple d'execució:
![Descripción de la imagen](/Imatges/5.png)

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    if opcio == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols auditar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "IpSSH-Especifica.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```

####**Opció 2 (Escaneig forçant IPv4):**

Aquesta opció et permet auditar la configuració de seguretat del servidor SSH amb una especificació clara de l'ús d'IPv4. El programa sol·licitarà que introdueixis la direcció IP de l'objectiu que desitges auditar.

Durant l'escaneig, ssh-audit analitzarà les versions del protocol SSH admeses, els algoritmes de xifrat utilitzats, les configuracions de claus i altres paràmetres de seguretat associats amb SSH. El resultat d'aquesta auditoria serà presentat en un informe detallat, proporcionant-te informació valuosa per avaluar la robustesa de la configuració de seguretat del servidor SSH.

Recordeu que aquesta opció pot ser útil si desitges assegurar-te que només s'utilitzi IPv4 durant l'escaneig de seguretat. Després de completar l'auditoria, els resultats es mostraran a la terminal i s'enviaran a través de Telegram per a una revisió i accions addicionals.

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    elif opcio == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols auditar:  ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaForçantIPv4.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-4", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```


####**Opció 3 (Escaneig amb depuració (debug)):**

Aquesta opció proporciona funcionalitats de depuració addicionals durant l'escaneig del servidor SSH. Quan seleccionis aquesta opció, el programa realitzarà un escaneig del servidor objectiu amb ssh-audit incorporant informació detallada de depuració.

Durant aquest escaneig, es recopilaran detalls extensos sobre el procés d'auditoria, com ara informació específica sobre cada pas realitzat per l'eina ssh-audit. Aquesta sortida de depuració pot ser útil per a diagnosticar problemes específics o entendre més a fons els processos interns de l'auditoria.

Com amb les altres opcions, proporcionaràs la direcció IP de l'objectiu i, després de l'escaneig, els resultats es mostraran a la terminal i s'enviaran a través de Telegram per a revisió i accions addicionals.

Aquesta opció pot ser especialment útil per als usuaris avançats que necessitin una comprensió més profunda del funcionament intern de ssh-audit i vulguin analitzar les dades de depuració per a fins d'optimització o solució de problemes.

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    elif opcio == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols auditar:  ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaAmbDebug.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-d", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```

####**Opció 4 (Mostrar la sortida en format JSON):**

Aquesta opció permet visualitzar la sortida de l'escaneig del servidor SSH en format JSON. En seleccionar aquesta opció, el programa realitzarà l'escaneig de la direcció IP de l'objectiu utilitzant ssh-audit i presentarà els resultats en un format estructurat JSON.

El format JSON facilita la interpretació programàtica dels resultats de l'auditoria, oferint una representació clara i ordenada de la informació. Això pot ser especialment útil si desitges processar els resultats amb altres eines o integrar-los en altres sistemes.

Com amb les opcions anteriors, introduiràs la direcció IP de l'objectiu i, després de l'escaneig, els resultats es mostraran a la terminal. A més, es proporcionarà la opció de enviar els resultats a través de Telegram per a una revisió i accions addicionals.

Aquesta opció és indicada per aquells que prefereixen una representació estructurada i programàtica dels resultats de l'auditoria, potser amb la intenció de processar-los posteriorment mitjançant altres eines o scripts.

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    elif opcio == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols auditar:  ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "AuditoriaJSON.txt")
            with open(output_file, "w") as output:
                subprocess.run(["ssh-audit", "-j", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```
####**Opció 5 (Escanejar tots els ports SSH oberts):**

Aquesta opció permet realitzar un escaneig exhaustiu de tots els ports SSH oberts al servidor. Quan seleccionis aquesta opció, el programa utilitzarà l'eina ssh-audit per escanejar tots els ports de la direcció IP de l'objectiu amb la finalitat d'identificar quins d'ells estan configurats com a ports SSH.

Durant l'escaneig, ssh-audit analitzarà la configuració de seguretat dels ports SSH oberts, presentant un informe detallat que inclourà informació sobre les versions del protocol SSH admeses, els algoritmes de xifrat utilitzats, les configuracions de claus i altres paràmetres de seguretat associats amb SSH en cadascun dels ports oberts.

Aquesta opció és especialment útil quan no es coneix prèviament quin port SSH està en ús o si el servidor utilitza diversos ports. Després de l'escaneig, els resultats es mostraran a la terminal i tindràs l'opció de enviar-los a través de Telegram per a una revisió i accions addicionals.

Seleccionar aquesta opció t'ajudarà a assegurar-te que tots els ports SSH oberts estan configurats adequadament en termes de seguretat.

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    elif opcio == '5':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols auditar:  ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "PortsSSH_Oberts.txt")
            output_text = ssh_audit_all_ports(target)  
            with open(output_file, "w") as output:
                output.write(output_text)  
            print("Contingut del fitxer:")
            print(output_text)  
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```

Aquesta és la funció que escaneja els ports d'una adreça IP específica. Ha sigut usada per aquesta opció.

```
    def ssh_audit_all_ports(target):
    used_ports = []  # Llista per emmagatzemar els ports en ús

    # Escanejar tots els ports SSH en el rang 1-65535
    for port in range(1, 65536):
        # Verificar si el port està en ús
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Temps d'espera per a la connexió (1 segon)
        resultat = sock.connect_ex((target, port))
        sock.close()

        if resultat == 0:
            used_ports.append(port)

    if not used_ports:
        return "No s'ha trobat cap servidor SSH en cap port."
    
    return "\n".join([f"Port {port} és utilitzat per SSH." for port in used_ports])
```

Finalment tenim l'opció 6 que permet sortir al menú principal.

![Descripción de la imagen](/Imatges/7.png)

![Descripción de la imagen](/Imatges/6.png)

```
elif opcio == '6':
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Tornant al menú principal....")
            time.sleep(1.5)
            os.system('clear' if os.name == 'posix' else 'cls')
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número d'opció vàlid.")
```

Cal comentar que cada vegada que executem una opció de les anomenades anteriorment, tornarem al submenú (menys la de tornar al menú principal).

**--------------------------------------------------------------------------------------------------------------**

En segon lloc tenim l'opció d'enumeració amb l'eina "enumforlinux"

Però, abans de veure el resultat de l'execució del codi i el codi adjunt, explicarem una mica qué es i per a que ha estat  dissenyada Enum4linux és una eina de seguretat informàtica dissenyada per a la enumeració i anàlisi de sistemes basats en el protocol SMB/CIFS. Aquesta utilitat està especialment destinada a la detecció d'informació rellevant en xarxes de Microsoft Windows. Enum4linux es caracteritza per la seva capacitat per a explorar i recopilar informació d'una manera eficient, ajudant els professionals de la seguretat a identificar vulnerabilitats i realitzar auditories de seguretat.

Per inicialitzar aquesta opició escriurem únicament el número 2.

![Descripción de la imagen](/Imatges/8.png)

Seguidament ficarem la IP de l'objectiu que li vulguèssim extreure les seves vulnerabilitats. 

![Descripción de la imagen](/Imatges/22.png)

Aquesta part del codi és la que fà referència a l'opció mencionada anteriorment:

```
    ip = input("Introdueix la IP que vols escanejar amb enum4linux: ")

# Nom del fitxer on es guardaran els resultats
output_file = "resultats_enum4linux.txt"

print("Proces de l'execució d'enum4linux aquestes tres linies no son un error")
print("Aquest proces tarda uns 30 segons")
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
```

Finalment un cop acabi l'execució del programa torna al menú principal.

**--------------------------------------------------------------------------------------------------------------**

La següent opció que hi ha per executar es l'escaneig Nmap.

Per executar aquesta opció només escribim el número que li pertoca, en aquest cas el número 3.

![Descripción de la imagen](/Imatges/10.png)

Llavors ens sortirà un submenú el cual ens 


![Descripción de la imagen](/Imatges/11.png)


##Text:

![Descripción de la imagen](/Imatges/12.png)

```
    if opcio == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            subnet = input("Introdueix la subxarxa que vols escanejar (p. ex. 192.168.1.0/24): ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "HostsDeLaXarxa.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "-sn", subnet], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```



##Aquesta opcio es reclipa el mateix missatge a les demes opcion a la 2, 3 i 4

![Descripción de la imagen](/Imatges/13.png)

##Text:
```
    elif opcio == '2':
        os.system('clear' if os.name == 'posix' else 'cls')
        target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
        current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        output_file = os.path.join(current_directory, "PortsOberts.txt")
        with open(output_file, "w") as output:
            subprocess.run(["nmap", "-p-", target], stdout=output)
            with open(output_file, "r") as file:
                print("Contingut del fitxer:")
                print(file.read())
        mi_bot = TelegramBot()
        mi_bot.enviar_document(output_file)
        os.remove(output_file)
```

##Text:

```
    elif opcio == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "Serveis&Versions.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "-sV", target], stdout=output)
                with open(output_file, "r") as file:
                    print("Contingut del fitxer:")
                    print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```

##Text:

```
    elif opcio == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            target = input("Introdueix la IP de l'objectiu que vols escanejar: ")
            print("Aquest procés pot trigar mes de 70 segons.")
            current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            output_file = os.path.join(current_directory, "Vulnerabilitats.txt")
            with open(output_file, "w") as output:
                subprocess.run(["nmap", "--script", "vuln", target], stdout=output)
                with open(output_file, "r") as file:
                    print("Contingut del fitxer:")
                    print(file.read())
            mi_bot = TelegramBot()
            mi_bot.enviar_document(output_file)
            os.remove(output_file)
```

##Per tornar al menu amb l'opcio 5:

![Descripción de la imagen](/Imatges/15.png)

**--------------------------------------------------------------------------------------------------------------**

##Text:

![Descripción de la imagen](/Imatges/15.png)

##Text:

![Descripción de la imagen](/Imatges/16.png)

##Text:

```
    objectiu = input("Introduïu l'objectiu (p. ex: iesebre.com -l 200 -b yahoo): ")

    # Utilizamos la ruta completa al script theHarvester.py
    comanda = f"python3 /app/MP14-Projecte/theHarvester/theHarvester.py -d {objectiu}"

    # Nom del fitxer on es guardaran els resultats
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
```

##Un cop executat el programa en tornara al menú principal:

**--------------------------------------------------------------------------------------------------------------**

##Text:

![Descripción de la imagen](/Imatges/17.png)

##Text:

![Descripción de la imagen](/Imatges/18.png)

##Text:

```
  # Demanar a l'usuari la IP que vol geolocalitzar
  ip_address = input("Introdueix la IP que vols geolocalitzar: ")

  # URL de la API de ipinfo.io
  api_url = f'https://ipinfo.io/{ip_address}/json'

  try:
      # Realitzar una solicitud GET a la API
      response = requests.get(api_url)

      if response.status_code == 200:
          data = response.json()

          # Extraure la informació de geolocalització
          ip = data['ip']
          city = data['city']
          region = data['region']
          country = data['country']
          location = data['loc']

          print(f'IP: {ip}')
          print(f'City: {city}')
          print(f'Region: {region}')
          print(f'Country: {country}')
          print(f'Location: {location}')
```

##Text:

 ![Descripción de la imagen](/Imatges/18.png)

##Un cop executat el programa en tornara al menú principal:

 **--------------------------------------------------------------------------------------------------------------**

##Text:

 ![Descripción de la imagen](/Imatges/19.png)

##Text:

 ![Descripción de la imagen](/Imatges/20.png)

##Text:

```
# Inicialitza el client de Shodan amb la clau API
api_key = 'EA2y81hle78OU28GmrhRJzbEzXZalgXd'
api = Shodan(api_key)

# Defineix la funció per obtenir el nom del servei
def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "Desconegut"

# Demana a l'usuari una direcció IP
ip = input("Introdueix una direcció IP: ")

# Obté la informació de la IP
ip_info = api.host(ip)

# Defineix el nom del fitxer on es guardarà la sortida
output_file = "shodan_resultats.txt"

# Obre el fitxer en mode d'escriptura i guarda la sortida
with open(output_file, "w") as file:
    # Escrivim els noms de domini associats a la IP
    file.write("Noms de domini associats a la IP:\n")
    for domain in ip_info['domains']:
        file.write(domain + "\n")

    # Escrivim els ports oberts trobats per Shodan i els seus noms de servei
    file.write("\nPorts trobats per Shodan:\n")
    for port_info in ip_info['data']:
        port = port_info['port']
        service_name = get_service_name(port)
        file.write(f"Port: {port} - Nom del servei: {service_name}\n")

# Mostra els resultats per terminal
with open(output_file, "r") as file:
    print("Contingut del fitxer:")
    print(file.read())
mi_bot = TelegramBot()
mi_bot.enviar_document(output_file)
os.remove(output_file)
```

 **--------------------------------------------------------------------------------------------------------------**



####**Finalment arribem a l'última opció del menú:** 

Amb l'ópcio número 7 sortirem del programa

  ![Descripción de la imagen](/Imatges/21.png)

---------------------------------------------------------------