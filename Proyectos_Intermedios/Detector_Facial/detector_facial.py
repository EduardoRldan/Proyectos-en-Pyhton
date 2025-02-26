import cv2
import mediapipe as mp

# Inicializar Mediapipe para detección de landmarks faciales
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Iniciar la cámara
camara = cv2.VideoCapture(0)

while True:
    _, frame = camara.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = face_mesh.process(frame_rgb)

    if resultados.multi_face_landmarks:
        for face_landmarks in resultados.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow("Reconocimiento Facial con Mediapipe", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
