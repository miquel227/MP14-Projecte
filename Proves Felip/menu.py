import subprocess

def escanear_red():
    print("Realizando escaneo de red...")
    # Aquí puedes agregar el código para realizar el escaneo de red utilizando Nmap u otra herramienta.

def main():
    while True:
        print("\nMenú:")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Escanear la red")
        print("5. Salir")

        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == "1":
            print("Has seleccionado la Opción 1.")
            # Aquí puedes agregar el código para la Opción 1.
        elif opcion == "2":
            print("Has seleccionado la Opción 2.")
            # Aqui pots agregar el codi per a l'opcio 2.
        elif opcion == "3":
            print("Has seleccionado la Opción 3.")
            # Aqui pots agregar el codi per a l'opcio 3.
        elif opcion == "4":
            escanear_red()  # Llama a la función para escanear la red.
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5).")

if __name__ == "__main__":
    main()