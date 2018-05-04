import cv2, sys, numpy, os
size = 4
fn_haar = 'haarcascade_frontalface_alt.xml'
fn_dir = 'att_faces/orl_faces'
# Part 1: Creando LBPHFaceRecognizer
print('Formando...')
# Crear una lista de imagenes y una lista de nombres correspondientes
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)
# Crear una matriz Numpy de las dos listas anteriores
(images, lables) = [numpy.array(lis) for lis in [images, lables]]
# OpenCV entrena un modelo a partir de las imagenes
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, lables)
# Part 2: Utilizar fisherRecognizer en funcionamiento la camara
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
while True:
    (rval, frame) = webcam.read()
    frame=cv2.flip(frame,1,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
    faces = haar_cascade.detectMultiScale(mini)
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        # Intentado reconocer la cara
        prediction = model.predict(face_resize)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # Escribiendo el nombre de la cara reconocida
        # La variable cara tendra el nombre de la persona reconocida
        cara = '%s' % (names[prediction[0]])
        if prediction[1]<110 :
          cv2.putText(frame,'%s - %.0f' % (cara,prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
          #En caso de que la cara sea de algun conocido se realizaras determinadas acciones
          #if cara == "CONOCIDO":
            #ACCIONES PARA CARAS CONOCIDAS
        elif prediction[1]>111 and prediction[1]<500:           
            #Si la cara es desconocida, poner desconocido
            cv2.putText(frame, 'Desconocido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))  
   

        cv2.imshow('OpenCV', frame)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break
