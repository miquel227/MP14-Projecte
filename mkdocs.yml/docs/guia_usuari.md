# Guia Usuari

###Requeriments per poder utilitzar el nostre programari.

+ Qualsevol Sistema Operatiu de Linux

+ <p>Docker Compose instal·lat (mira <a href="https://docs.docker.com/engine/install/" title="Title">Instalar Docker Compose)</a></p>

+ Potser també una tasa de cafe o de te :)



```python

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

