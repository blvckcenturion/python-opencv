import numpy as np
import time
import cv2
# Cesar Suarez

# tarea: probar el seguidor de colores con otras opciones de color
# Green 
GreenLower = np.array([30, 150, 0], dtype = "uint8")
GreenUpper = np.array([25, 255, 30], dtype = "uint8")
# Black
BlackLower = np.array([20, 20, 20], dtype = "uint8")
BlackUpper = np.array([0, 0, 0], dtype = "uint8")
# Red
RedLower = np.array([67, 100, 0], dtype = "uint8")
RedUpper = np.array([255, 128, 50], dtype = "uint8")


# Computacion Grafica y Robotica
# define los limites superior e inferior de un color
# para ser considerado "azul"
blueLower = np.array([100, 67, 0], dtype = "uint8")
blueUpper = np.array([255, 128, 50], dtype = "uint8")
# cargar video
camera = cv2.VideoCapture(0)
# podemos leer frames de un video
#camera = cv2.VideoCapture('\video\azul1.avi')
# mantener el bucle
while True:
	# agarrar el marco actual
	(grabbed, frame) = camera.read()
	# verificar para ver si hemos llegado al final del video si pasamos un video
	if not grabbed:
		break
	# determinar que pixeles caen dentro de los limites azules
	# y luego desenfocar la imagen binaria
	blue = cv2.inRange(frame, blueLower, blueUpper)
	# QUE HACE LA FUNCION GAUSSIANBLUR ??????????
    # Applies Gaussian Smoothing on the input source image
    # Gaussian Smoothing help in reducing the noise captured by the camera sensor.
	blue = cv2.GaussianBlur(blue, (3, 3), 0)
	# encontrar contornos en la imagen
	# COMO FUNCIONA LA FUNCION CONTOURS
	(cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	# verificar para ver si se encontraron contornos
	if len(cnts) > 0:
		# ordenar los contornos y encontrar el mas grande
		# asumira que este contorno corresponde al area ES VERDAD ??????
		cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
		# Calcular el cuadro delimitador y dibujarlo
		rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
		cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
	# mostrar el marco y la imagen binaria
	cv2.imshow("Tracking", frame)
	cv2.imshow("Binary", blue)
	# Se pueden mostrar los marcos en "avance rapido"
	# 32 marcos por segundo
	# con un simple truco podemos generar un retraso entre fotogramas;
	# Si su computadora es lenta, es probable que desee
	# descomentar la siguiente linea
	#time.sleep(0.025)
	# si se presiona la tecla 'q', se detiene el ciclo
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
# limpiar la camara y cerrar las ventanas abiertas
camera.release()
cv2.destroyAllWindows()