import cv2
import dlib

# Cargar el detector de rostros y el predictor de landmarks
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Ruta al modelo

# Iniciar la cámara
camara = cv2.VideoCapture(0)

while True:
    # Capturar frame de la cámara
    _, frame = camara.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    
    # Detectar rostros
    rostros = detector(gris)

    for rostro in rostros:
        # Dibujar el rectángulo del rostro
        x, y, w, h = rostro.left(), rostro.top(), rostro.width(), rostro.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Obtener los puntos clave del rostro
        landmarks = predictor(gris, rostro)

        # Dibujar los puntos clave en la cara
        for i in range(68):
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

    # Mostrar el video en una ventana
    cv2.imshow("Reconocimiento Facial con Landmarks", frame)

    # Presionar "q" para salir
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
