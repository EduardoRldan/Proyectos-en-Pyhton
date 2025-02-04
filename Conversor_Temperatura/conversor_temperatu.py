def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9


def celsius_a_kelvin(c):
    return (c + 273.15)


print("1) Celsius a Fahrenheit")
print("2) Fahrenheit a Celsius")
print("3) Celsius a Kelvin")


opcion = input("Elige una opción: ")
temp = float(input("Ingrese la temperatura: "))

if opcion == '1':
    print("Resultado:", celsius_a_fahrenheit(temp), "°F")
elif opcion == '2':
    print("Resultado:", fahrenheit_a_celsius(temp), "°C")
elif opcion == '3':
    print("Resultado:", celsius_a_kelvin(temp), "K")
else:
    print("Opción inválida.")