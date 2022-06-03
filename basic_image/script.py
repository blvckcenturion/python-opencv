import cv2

image = cv2.imread("./images/jurasic.jpg")
# Loading the image, then destructuring the height and width of the image from the image's shape attribute.
# :2 takes the last two elements of the tuple. 
(h, w) = image.shape[:2]

cv2.imshow("Original", image)
# The left top pixel is at (0, 0) of the image returned by the cv2.imread() function.
# In the next line we destructure the red, green and blue values of the pixel at (0, 0) and print them.
(b, g, r) = image[0, 0]

# que hace la siguiente linea de codigo (9)? ........
# Printing the values of red, green and blue taken from the left top pixel(0,0)
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# ahora, cambiemos el valor del pixel en (0, 0) y hagamos que sea rojo  es verdad ? analicen el codigo........
# In this case by assigning (255,0,0) to the pixel will make it blue due to the order used in openCV
image[0, 0] = (255, 0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# calcular el centro de la imagen, que es simplemente el ancho y la altura
# dividiendo por dos ?......

(cX, cY) = (w // 2, h // 2)
# We can prove that by performing the operation above we get as a result the center of each axis
print(f"width: {w} | center X: {cX}")
print(f"height: {h} | center X: {cY}")
# ya que estamos usando matrices NumPy ??????, podemos aplicar cortes y obtener partes
# de la imagen a partir de la esquina superior izquierda, es cierto ????????????

# The image is a NumPy array
# And the stated argument is true
# Becase we are getting the values from position 0, until position cX & cY.
tl = image[0:cY, 0:cX]
cv2.imshow("esquina superior-izquierda", tl)

# de forma similar, agarremos la parte superior derecha, la inferior derecha y la inferior izquierda
# cada parte la mostramos en pantalla
# Upper Right Corner 
tr = image[0:cY, cX:w]
# Lower Right Corner 
br = image[cY:h, cX:w]
# Upper Left Corner
bl = image[cY:h, 0:cX]
cv2.imshow("esquina superior-derecha", tr)
cv2.imshow("esquina inferior-derecha", br)
cv2.imshow("esquina inferior izquierda", bl)

# ahora vamos a hacer que la esquina superior izquierda de la imagen original este verde,  es verdad ?.........
# In the next line we change the values of the upper left corner to blue, so the statement made in the upper line is false.
image[0:cY, 0:cX] = (509, 0,0)

# Showing the updated image
cv2.imshow("actualizada", image)
cv2.waitKey(0)
