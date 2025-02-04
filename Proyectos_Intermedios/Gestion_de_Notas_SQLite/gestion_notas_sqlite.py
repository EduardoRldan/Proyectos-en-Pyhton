import sqlite3
from tabulate import tabulate

# conectar a la base de datos Sqlite 
conn = sqlite3.connect("notas.db")
cursor = conn.cursor()


# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        asignatura TEXT NOT NULL,
        nota REAL NOT NULL
    )
""")
conn.commit()

# Función para agregar una nota
def agregar_nota():
    nombre = input("Nombre del estudiante: ")
    asignatura = input("Asignatura: ")
    nota = float(input("Nota: "))
    cursor.execute("INSERT INTO estudiantes (nombre, asignatura, nota) VALUES (?, ?, ?)", (nombre, asignatura, nota))
    conn.commit()
    print("✅ Nota agregada exitosamente.")

# Función para mostrar todas las notas
def mostrar_notas():
    cursor.execute("SELECT * FROM estudiantes")
    registros = cursor.fetchall()
    if registros:
        print(tabulate(registros, headers=["ID", "Nombre", "Asignatura", "Nota"], tablefmt="grid"))
    else:
        print("No hay registros en la base de datos.")

# Función para actualizar una nota
def actualizar_nota():
    mostrar_notas()
    id_estudiante = int(input("ID del estudiante a actualizar: "))
    nueva_nota = float(input("Nueva nota: "))
    cursor.execute("UPDATE estudiantes SET nota = ? WHERE id = ?", (nueva_nota, id_estudiante))
    conn.commit()
    print("✅ Nota actualizada correctamente.")

# Función para eliminar una nota
def eliminar_nota():
    mostrar_notas()
    id_estudiante = int(input("ID del estudiante a eliminar: "))
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conn.commit()
    print("✅ Registro eliminado correctamente.")

# Menú interactivo
while True:
    print("\n📌 Sistema de Gestión de Notas")
    print("1️⃣ Agregar Nota")
    print("2️⃣ Mostrar Notas")
    print("3️⃣ Actualizar Nota")
    print("4️⃣ Eliminar Nota")
    print("5️⃣ Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        agregar_nota()
    elif opcion == "2":
        mostrar_notas()
    elif opcion == "3":
        actualizar_nota()
    elif opcion == "4":
        eliminar_nota()
    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida. Intenta de nuevo.")

# Cerrar conexión
conn.close()