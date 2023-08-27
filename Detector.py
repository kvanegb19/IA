# Librería para el procesamiento de imágenes en tiempo real
import cv2

# Obtener la imagen del webcam
# https://es.acervolima.com/como-obtener-las-propiedades-del-objeto-python-cv2-videocapture/
capture = cv2.VideoCapture(0)

#si se quiere utilizar la cámara del celular
ip="http://192.168.100.142:4747/video"
capture.open(ip)

# Utilizar el clasificador proporcionado por la herramienta Cascade-Trainer-GUI
# https://docs.opencv.org/4.3.0/dc/d88/tutorial_traincascade.html
clasificador_objeto = cv2.CascadeClassifier('cascade.xml')

# estructura de repetición para activar la camara y la toma de imágenes
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# https://github.com/opencv/opencv/tree/master/data/haarcascades
while True:
	# Capturar vídeo de la cámara------------------------------------
	ret,frame = capture.read()
	# Obtener la imagen del frame y convertir a escala de grises
	# https://es.acervolima.com/python-opencv-metodo-cv2-cvtcolor/
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Ahora se procede aplicar y utilizar el clasificador generado por la herrameinta

	test_object = clasificador_objeto.detectMultiScale(image,
	# https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
	# scaleFactor = 11,
	# minNeighbors = 91,
	# minSize=(50,78))
	scaleFactor = 11,
	minNeighbors = 100,
	minSize=(80,80))
	
	# Si el rostro es detectado se obtienes los valores 
	for (x,y,w,h) in test_object:
		# Se procede a dibujar el rectangulo
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		# Se procede a crear el texto 
		cv2.putText(frame,'detectado',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

	# Presentar el frame
	cv2.imshow('frame',frame)
	# Detener la camara presionando la tecla ESC (ascii==27)
	if cv2.waitKey(1) == 27:
		break

# Mostrar el frame
capture.release()
# Limpiar todas las ventanas
cv2.destroyAllWindows()