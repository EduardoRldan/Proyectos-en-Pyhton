def cifrar_cesar(texto, desplazamiento):
    cifrado = ''
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            cifrado += chr((ord(letra) - base + desplazamiento) % 26 + base)
        else:
            cifrado += letra
    return cifrado

mensaje = input("Ingrese el mensaje: ")
desplazamiento = int(input("Ingrese el número de desplazamiento: "))
print("Mensaje cifrado:", cifrar_cesar(mensaje, desplazamiento))
