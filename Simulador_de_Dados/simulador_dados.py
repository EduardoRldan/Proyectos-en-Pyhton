import random

def lanzar_dado():
    return random.randint(1, 6)

while True:
    input("\nPresiona Enter para lanzar el dado...")
    print("🎲 Resultado:", lanzar_dado())

    if input("¿Quieres lanzar otra vez? (s/n): ").lower() != 's':
        break
