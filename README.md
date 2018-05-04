# Reconocimiento facial con OPENCV
OPENCV tiene 3 metodos incorporados para realizar reconocimiento facial, y porque **#Python** podemos usar cualquiera de ellos solo cambiando una linea de codigo. Aqui los 3 metodos y como llamarlos:

1. EigenFaces – cv2.face.EigenFaceRecognizer_create()
2. FisherFaces – cv2.face.FisherFaceRecognizer_create()
3. Local Binary Patterns Histograms (LBPH) – cv2.face.LBPHFaceRecognizer_create()

Cada uno resalta componentes principales diferentes, es cuestion de elegir el adecuado de acuerdo a las necesidades de cada proyecto.

| **EigenFaces** | **FisherFaces** | **LBPH** |
| :-------: | :------: | :-----: |
| <img src="https://docs.opencv.org/2.4/_images/eigenfaces_opencv.png" width="200">|<img src="https://docs.opencv.org/2.4/_images/fisherfaces_opencv.png" width="200">|<img src="https://docs.opencv.org/2.4/_images/lbp_yale.jpg" width="200">|
