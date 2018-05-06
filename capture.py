import cv2, sys, numpy, os

size = 4
dir_faces = 'att_faces/orl_faces'
fn_name = sys.argv[1]
path = os.path.join(dir_faces, fn_name)

if not os.path.isdir(path):
    os.mkdir(path)
    
img_width, img_height = 112, 92
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

count = 0
while count < 100:
    rval, img = cap.read()
    img = cv2.flip(img, 1, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
    faces = face_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (img_width, img_height))
        pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
               if n[0]!='.' ]+[0])[-1] + 1
        cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(img, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
            1,(0, 255, 0))
        count += 1
    cv2.imshow('OpenCV Entrenamiento', img)
    key = cv2.waitKey(10)
    if key == 27:
        break
