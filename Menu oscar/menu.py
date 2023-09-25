import subprocess

def escanejar_xarxa():
    print("Realitzant l'escaneig de xarxa...")
    # Aquí pots afegir el codi per realitzar l'escaneig de xarxa utilitzant Nmap o una altra eina.

def opcio1_submenu():
    while True:
        print("\nSubmenú - Opció 1:")
        print("1. Fer-ho amb Shodan")
        print("2. Fer-ho amb Nmap")
        print("3. Tornar al menú principal")

        opcio = input("Selecciona una opció (1/2/3): ")

        if opcio == "1":
            print("Has seleccionat fer-ho amb Shodan.")
            # Aquí pots afegir el codi per fer-ho amb Shodan.
        elif opcio == "2":
            print("Has seleccionat fer-ho amb Nmap.")
            # Aquí pots afegir el codi per fer-ho amb Nmap.
        elif opcio == "3":
            print("Tornant al menú principal.")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida (1/2/3).")

def main():
    while True:
        print("\nMenú:")
        print("1. Opció 1")
        print("2. Opció 2")
        print("3. Opció 3")
        print("4. Escanejar la xarxa")
        print("5. Sortir")

        opcio = input("Selecciona una opció (1/2/3/4/5): ")

        if opcio == "1":
            print("Has seleccionat l'Opció 1.")
            opcio1_submenu()  # Mostrar submenú per l'Opció 1.
        elif opcio == "2":
            print("Has seleccionat l'Opció 2.")
            # Aquí pots afegir el codi per a l'Opció 2.
        elif opcio == "3":
            print("Has seleccionat l'Opció 3.")
            # Aquí pots afegir el codi per a l'Opció 3.
        elif opcio == "4":
            escanejar_xarxa()  # Truca a la funció per escanejar la xarxa.
        elif opcio == "5":
            print("Sortint del programa. Fins aviat!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida (1/2/3/4/5).")

if __name__ == "__main__":
    main()
