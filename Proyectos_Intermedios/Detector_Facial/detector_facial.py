import cv2

cascade_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error: No se puede acceder a la cámara. ")
    exit()

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error al momento de la captura del frame. ")
        break


    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertidor a escala de grises

    # Detector de rostros
    rostros = cascade_rostro.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujado del rectangulo 
    for (x,y,w,h) in rostros:
        cv2.rectangle(frame, (x ,y), (x + w, y + h), (0 , 255, 0,2))

    # Mostrar el video en pantalla
    cv2.imshow("Detector Facial", frame)

    # Presionar la letra q para salir del programa 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cierre del programa
camara.release()
cv2.destroyAllWindows()