tareas = []

def mostrar_tareas():
    if not tareas:
        print("\nNo hay tareas en la lista.")
    else:
        print("\nLista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


def agregar_tarea():
    tarea = input("\nIngrese la nueva tarea:")
    tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingrese un número válido.")

while True:
    print("\nMenú: 1) Ver tareas  2) Agregar  3) Eliminar  4) Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        mostrar_tareas()
    elif opcion == '2':
        agregar_tarea()
    elif opcion == '3':
        eliminar_tarea()
    elif opcion == '4':
        break
    else:
        print("Opción inválida.")