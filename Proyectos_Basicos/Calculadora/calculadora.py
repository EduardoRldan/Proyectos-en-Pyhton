import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raiz de un número negativo"
    return math.sqrt(a)

while True:
    print("n\📌 Calculadora Mejorada 🧮")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz Cuadrada")
    print("7. Salir")

    opcion = input("Selecciona una opción (1-7): ")

    if opcion == "7":
        print("Saliendo..... !Hasta Luego¡")
        break


    if opcion in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Ingresa el número para la raíz cuadrada: "))
        num2 = None


    if opcion == "1":
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        print("Resultado:", division(num1, num2))
    elif opcion == "5":
        print("Resultado:", potencia(num1, num2))
    elif opcion == "6":
        print("Resultado:", raiz_cuadrada(num1))
    else:
        print("Opción no válida. Intenta de nuevo.")