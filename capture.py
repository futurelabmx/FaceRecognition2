#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
#Obtener el nombre de la persona que estamos capturando
import sys
nombre = sys.argv[1]

#Directorio donde se encuentra la carpeta con el nombre de la persona
dir_faces = 'att_faces/orl_faces'
path = os.path.join(dir_faces, nombre)

#Tamaño para reducir a miniaturas las fotografias
size = 4

#Si no hay una carpeta con el nombre ingresado entonces se crea
if not os.path.isdir(path):
    os.mkdir(path)

#cargamos la plantilla e inicializamos la webcam
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

img_width, img_height = 112, 92

#Ciclo para tomar fotografias
count = 0
while count < 100:
    #leemos un frame y lo guardamos
    rval, img = cap.read()
    img = cv2.flip(img, 1, 0)

    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #redimensionar la imagen
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    """buscamos las coordenadas de los rostros (si los hay) y
   guardamos su posicion"""
    faces = face_cascade.detectMultiScale(mini)    
    faces = sorted(faces, key=lambda x: x[3])
    
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (img_width, img_height))
        
        #Dibujamos un rectangulo en las coordenadas del rostro
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #Ponemos el nombre en el rectagulo
        cv2.putText(img, nombre, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))        

        #El nombre de cada foto es el numero del ciclo
        #Obtenemos el nombre de la foto
        #Despues de la ultima sumamos 1 para continuar con los demas nombres
        pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
               if n[0]!='.' ]+[0])[-1] + 1

        #Metemos la foto en el directorio
        cv2.imwrite('%s/%s.png' % (path, pin), face_resize)

        #Contador del ciclo
        count += 1

    #Mostramos la imagen
    cv2.imshow('OpenCV Entrenamiento de '+nombre, img)

    #Si se presiona la tecla ESC se cierra el programa
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break
