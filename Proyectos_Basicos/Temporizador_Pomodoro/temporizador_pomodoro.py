import time 

def temporizador(segundos):
    while segundos:
        mins, sec = divmod(segundos, 60)
        print(f"\r⏳ Tiempo restante: {mins:02}:{sec:02}", end ="")
        time.sleep(1)
        segundos -=1
    print("\n⏰ !Tiempo terminado¡")


tiempo = int(input("Ingrese el tiempo en segundos"))
temporizador(tiempo)