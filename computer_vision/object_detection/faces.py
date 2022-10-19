import numpy as np
import cv2

def iniciar_detectores():
    face_cascade = cv2.CascadeClassifier()
    face_cascade.load("computer_vision/object_detection/cascade/haarcascade_frontalface_alt.xml")

    eyes_cascade = cv2.CascadeClassifier()
    eyes_cascade.load("computer_vision/object_detection/cascade/haarcascade_eye_tree_eyeglasses.xml")

    return face_cascade, eyes_cascade

def detectar_rostros(img, face_cascade, eyes_cascade):
    img2 = img.copy()
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray)

    # para cada rostro detectado
    # box: x, y, w, h
    for x, y, w, h in faces:
            center = (x + w//2, y + h//2)
            img2 = cv2.ellipse(img2, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

            face_ROI = gray[y:y + h, x:x + w]
            # detectar ojos
            eyes = eyes_cascade.detectMultiScale(face_ROI)

            for x2, y2, w2, h2 in eyes:
                    eye_center = (x + x2 + w2//2,y + y2 + h2//2)
                    r = int(round((w2 + h2) * 0.25))
                    img2 = cv2.circle(img2, eye_center, r, (0, 255, 0), 3)
    return img2


cap = cv2.VideoCapture(0)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")
    
f_c, e_c = iniciar_detectores()

while True:
    # lectura de un frame
    ret, frame = cap.read()
    # operaciones con el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out = detectar_rostros(frame, f_c, e_c)
    # mostrar imagenes en una ventana
    cv2.imshow("input", frame)
    cv2.imshow("output", out)

    # detectar una tecla
    c = cv2.waitKey(1)
    # si la tecla es 'esc'
    if c == 27: 
        # salir del bucle
        break

# liberar recursos
cap.release()
cv2.destroyAllWindows()