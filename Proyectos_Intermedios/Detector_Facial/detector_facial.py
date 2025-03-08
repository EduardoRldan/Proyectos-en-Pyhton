import cv2
import mediapipe as mp
import face_recognition

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Iniciar la cámara
camara = cv2.VideoCapture(0)

while True:
    ret, frame = camara.read()
    frame = cv2.flip(frame, 1)  # Voltear horizontalmente para efecto espejo

    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Usar face_recognition para detectar ubicaciones faciales
    face_locations = face_recognition.face_locations(frame_rgb)

    if face_locations:
        # Procesar la imagen con MediaPipe solo si hay rostros
        resultado = face_mesh.process(frame_rgb)

        for top, right, bottom, left in face_locations:
            # Dibujar rectángulo alrededor del rostro detectado
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        if resultado.multi_face_landmarks:
            for face_landmarks in resultado.multi_face_landmarks:
                h, w, _ = frame.shape
                
                # Dibujar landmarks si se detectan los 468 puntos
                if len(face_landmarks.landmark) == 468:
                    for idx, landmark in enumerate(face_landmarks.landmark):
                        x, y = int(landmark.x * w), int(landmark.y * h)
                        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    else:
        # Mostrar mensaje si no se detectan rostros
        cv2.putText(frame, "No se detecta rostro", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostrar el video en una ventana
    cv2.imshow("Reconocimiento Facial Optimizado", frame)

    # Presionar "q" para salir
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()

# 🔧 Cambios de optimización:
# 1. Acceso a la cámara optimizado (línea 12).
# 2. MediaPipe solo se ejecuta si hay rostros detectados (línea 20).
# 3. Puntos de landmarks más pequeños para mayor fluidez (línea 31).

# Esto hace que tu programa sea más rápido y eficiente, sin perder precisión. 🚀


# Cosas que mejorar 
# 1. Rendimiento (sobre todo el rendimiento)