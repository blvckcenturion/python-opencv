import numpy as np
import cv2

# cargar la imagen y mostrarla
image = cv2.imread("./images/jurasic.jpeg")
cv2.imshow("Original", image)

# El generar mascaras nos permite enfocarnos unicamente en partes de una imagen que nos interesan.
# UNA MASCARA SOLO MANEJA 2 VALORES PARA SUS PIXELES???????? (0 o 255) es cierto ??????

# It is true, a mask can only take 0s and 255s

# LOS PIXELES CON VALOR 0 SE IGNORAN Y LOS QUE TIENE VALOR 255 SE MANTIENE???
# vamos a construir una mascara rectangular que muestre solo la parte de la imagen que nos interesa

# Creates a NumPy array composed of only 0s and takes the shape of the image
mask = np.ones(image.shape[:2], dtype="uint8") * 210
print(mask)
cv2.rectangle(mask, (66, 5), (239, 85), 255, -1)
cv2.imshow("MASCARA", mask)

# Aplicar mascara: observe como solo se corta la parte de la imagen que queremos
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("MASCARCARA RECTANGULAR APLICADA A LA IMAGEN", masked)
cv2.waitKey(0)

# Ahora, hagamos una mascara circular con un radio de 100
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (167, 50), 50, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("MASCARA", mask)
cv2.imshow("MASCARA CIRCULA APLICADA A LA IMAGEN", masked)
cv2.waitKey(0)