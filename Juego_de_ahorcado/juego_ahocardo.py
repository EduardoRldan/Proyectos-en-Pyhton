import random

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    return ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

def jugar_ahorcado():
    palabras = ["python", "programacion", "juego", "ahorcado", "computadora"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = set()
    intentos = 6  # Número de intentos antes de perder

    print("¡Bienvenido al juego del ahorcado!")
    
    while intentos > 0:
        print("\nPalabra:", mostrar_palabra_oculta(palabra_secreta, letras_adivinadas))
        letra = input("Ingrese una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya intentaste con esa letra.")
        elif letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Bien! Letra correcta.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if set(palabra_secreta) == letras_adivinadas:
            print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            return

    print("\n¡Perdiste! La palabra era:", palabra_secreta)

# Iniciar el juego
jugar_ahorcado()
