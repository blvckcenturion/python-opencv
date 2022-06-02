import cv2

image = cv2.imread("jurasic.jpg")
# Loading the image, then destructuring the height and width of the image from the image's shape attribute.
# :2 takes the last two elements of the tuple. 
(h, w) = image.shape[:2]

cv2.imshow("Original", image)
# The left top pixel is at (0, 0) of the image returned by the cv2.imread() function.
# In the next line we destructure the red, green and blue values of the pixel at (0, 0) and print them.
(b, g, r) = image[0, 0]
# que hace la siguiente linea de codigo (9)? ........

print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# ahora, cambiemos el valor del pixel en (0, 0) y hagamos que sea rojo  es verdad ? analicen el codigo........
image[0, 0] = (255, 0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# calcular el centro de la imagen, que es simplemente el ancho y la altura
# dividiendo por dos ?......
(cX, cY) = (w // 2, h // 2)
# ya que estamos usando matrices NumPy ??????, podemos aplicar cortes y obtener partes
# de la imagen a partir de la esquina superior izquierda, es cierto ????????????
tl = image[0:cY, 0:cX]
cv2.imshow("esquina superior-izquierda", tl)
# de forma similar, agarremos la parte superior derecha, la inferior derecha y la inferior izquierda
# cada parte la mostramos en pantalla
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("esquina superior-derecha", tr)
cv2.imshow("esquina inferior-derecha", br)
cv2.imshow("esquina inferior izquierda", bl)
# ahora vamos a hacer que la esquina superior izquierda de la imagen original este verde,  es verdad ?.........
image[0:cY, 0:cX] = (255, 0,0)
# Mostramos nuestra imagen actualizada
cv2.imshow("actualizada", image)
cv2.waitKey(0)
