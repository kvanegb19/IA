# Librería para el procesamiento de imágenes en tiempo real
import cv2
# Librería  especializada en el cálculo numérico y el análisis de datos
import numpy as np
# Librería para el manejo de archivos del Sistema Operativo
import os

# Establecer el directorio donde se van almacenar las imágenes postivivas y negativas 
Datos = 'p' # n
# Verifica la existencia del directorio
if not os.path.exists(Datos):
	# Realiza la creación de la carpeta
	os.makedirs(Datos)
	print('Carpeta creada: ', Datos)
	
# Obtener la imagen del webcam
capture = cv2.VideoCapture(0)

#si se quire utilizar la cámara del celular
ip="http://192.168.100.142:4747/video"
capture.open(ip)


# variable para incrementar las imagenes a guardar 
count = 1
# estructura de repetición para activar la camara y la toma de imágenes
while True:
	# Capturar vídeo de la cámara------------------------------------
	ret, frame = capture.read()
	# Capturar vídeo de la cámara------------------------------------
	if ret == False:  break

	# Establecer las dimensiones para el rectangulo
    # t.ly/ttPJ
	x1, y1 = 190, 80
	x2, y2 = 450, 398
	# Dibujar el triangulo con las anteriores dimensiones
	cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

	# Ahora se obtiene un nuevo frame para capturar lo que esta en el cuadro rojo
	imAux = frame.copy()
	# Establecer las dimensiones para el frame_auxiliar
	frame_auxiliar = imAux[y1:y2,x1:x2]
	# especificar las nuevas dimensiones para el frame_auxiliar
	width = 38
	height = 38
	dim = (width, height)
	# Redimenzionar el nuevo frame con las medidas establecidas
	frame_auxiliar = cv2.resize(frame_auxiliar, dim, interpolation = cv2.INTER_AREA)


	# Se establece la captura de la imagen
	if cv2.waitKey(1) == ord('s'):
		# Se establece el método para guardar la imágen 
		# t.ly/dQeJ
		# t.ly/LUFb
		cv2.imwrite(Datos+'/frame_auxiliar{}.jpg'.format(count),frame_auxiliar)
		print('Imagen almacenada: ', 'frame_auxiliar{}.jpg'.format(count))
		# permitir que el contador se incremente
		count = count + 1
	# Capturar vídeo de la cámara------------------------------------ 
	if cv2.waitKey(1) == ord('q'): 
		break
	# Presentar el frame
	cv2.imshow('frame',frame)
	# Presentar el frame_auxiliar
	cv2.imshow('objeto',frame_auxiliar)

# Mostrar el frame
capture.release()
# Limpiar todas las ventanas
cv2.destroyAllWindows()