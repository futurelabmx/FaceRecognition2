# Reconocimiento facial con OPENCV
Mediante el uso de un script aprenderemos las caras que nos interesen y con otro script arrancaremos la función de reconocimiento.

OPENCV tiene 3 metodos incorporados para realizar reconocimiento facial, y porque **#Python** podemos usar cualquiera de ellos solo cambiando una linea de codigo. Aqui los 3 metodos y como llamarlos:

1. EigenFaces – cv2.face.EigenFaceRecognizer_create()
2. FisherFaces – cv2.face.FisherFaceRecognizer_create()
3. Local Binary Patterns Histograms (LBPH) – cv2.face.LBPHFaceRecognizer_create()

Cada uno resalta componentes principales diferentes, es cuestion de elegir el adecuado de acuerdo a las necesidades de cada proyecto.

| **EigenFaces** | **FisherFaces** | **LBPH** |
| :-------: | :------: | :-----: |
| <img src="https://docs.opencv.org/2.4/_images/eigenfaces_opencv.png" width="200">|<img src="https://docs.opencv.org/2.4/_images/fisherfaces_opencv.png" width="200">|<img src="https://docs.opencv.org/2.4/_images/lbp_yale.jpg" width="200">|

# Como usar la herramienta
Para empezar deberemos instalar OpenCV junto con todas sus dependencias ⚠ Numpy y contrib son importantes ⚠ 
~~~
pip install opencv-contrib-python
~~~

Posteriormente para guardar las fotos de entrenamiento para el modelo, nos descargaremos una pequeña BD de caras para que tenga mejor precisión y a la que añadiremos nuestra cara o las que nos interesen. Nos bajamos la BD de ejemplo de la Database of Faces de AT&T Laboratories Cambridge, descomprimimos la carpeta, dentro de ella creamos una mas llamada orl_faces y dentro de esa creamos una carpeta con el nombre de las caras que queremos reconocer. La ruta seria algo como esto:
~~~
carpeta_de_proyecto\att_faces\orl_faces\luis_sustaita
carpeta_de_proyecto\att_faces\orl_faces\antonio_smith
carpeta_de_proyecto\att_faces\orl_faces\ricardo_ferro
carpeta_de_proyecto\att_faces\orl_faces\rodolfo_miron
~~~

De los scripts uno será para aprender caras (capture.py) y el otro para reconocerlas (reconocimiento.py).

El primero de ellos es simple: busca una cara, toma una foto de ella y la guarda en la carpeta correspondiente.
~~~
python capture.py nombrePersona
~~~
<img src="https://github.com/futurelabmx/FaceRecognition2/blob/master/entrenamiento.png?raw=true" width="600">

- ⚠Ten en cuenta que el nombre de la persona es el mismo que pusiste en el nombre de su carpeta.

- 👌Por default el script toma 100 fotos del rostro, pero recuerda que entre mayor sea el entrenamiento mejores reultados se obtendran.

- ☝Trata de que solo una parsona aparezca en la escena para no guardar otros rostros con la misma etiqueta o nombre.

Para comenzar a detectar y reconocer caras:
~~~
python reconocimiento.py
~~~
- Puedes cambiar el metodo de reconocimiento por caulquiera de los 3 mencionados al inicio, prueba los 3 y checa cual te da mejores resultados.

<img src="https://github.com/futurelabmx/FaceRecognition2/blob/master/reconocido.png" width="600">
