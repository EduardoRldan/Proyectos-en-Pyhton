import cv2

# Cargar el clasificador de rostros de OpenCV (Haar Cascade)
cascade_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Iniciar la cámara
camara = cv2.VideoCapture(0)

while True:
    # Capturar frame de la cámara
    _, frame = camara.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    
    # Detectar rostros en la imagen
    rostros = cascade_rostro.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el video en una ventana
    cv2.imshow("Reconocimiento Facial", frame)

    # Presionar "q" para salir
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
