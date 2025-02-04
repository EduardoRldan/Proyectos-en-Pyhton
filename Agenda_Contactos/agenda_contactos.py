def agregar_contacto():
    with open("contactos.txt", "a") as file:
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        file.write(f"{nombre},{telefono}\n")
        print("Contacto guardado.")

def mostrar_contactos():
    try:
        with open("contactos.txt", "r") as file:
            print("\nLista de Contactos:")
            for linea in file:
                nombre, telefono = linea.strip().split(',')
                print(f"{nombre}: {telefono}")
    except FileNotFoundError:
        print("No hay contactos guardados.")

while True:
    print("\n1) Agregar Contacto  2) Ver Contactos  3) Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        mostrar_contactos()
    elif opcion == '3':
        break
    else:
        print("Opción inválida.")
