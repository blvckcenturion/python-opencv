import numpy as np
import cv2

# load the image and show it 
image = cv2.imread("./images/grand_canyon.png")
cv2.imshow("Original", image)
# The images are NumPy arrays stored as 8 bit unsigned integers
# Los valores de nuestros pixeles estaran en el rango [0, 255]  QUE OPINA ????????? ES ASI?????

# The value of the pixel is not in range of 255 as a each pixel
# is represented as a tuple containing 3 values (b,g,r) which they go from 0 to 255

# Using functions like cv2.add y cv2.subtract, the values are going to be added or subtracted to the range we are working with.
# QUE SUCEDE SI LOS VALORES ADICIONADOS O RESTADOS ESTAN FUERA DEL RANGO [0, 255]. ?????????
# If the result of the add is 255+ it will set it as 255
# If the result of the subtract is 0- it will set it as 0

# COMENTA QUE HACEN LAS SIGUIENTES 2 LINEAS DE CODIGO
# First line we are adding 200 + 100 using openCV's add function and then printing the result
# Which in this case returns 255 as it is the value it defaults to
print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))

# Second line we are subtracting 50 - 100 using openCV's subtract function and then printing the result
# Which in this case returns 0 as it is the value it defaults to
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))

# Si se utiliza operaciones aritmeticas en estas matrices que sucede con los valores????
#   QUE HACE EL WRAP AROUND ???? QUE SUCEDE CON LAS DISTANCIAS??
#  ES IMPORTANTE TENER EN CUENTA TODOS ESTOS FACTORES CUANDO TRABAJAMOS CON IMAGENES?
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

# aumentemos la intensidad de todos los pixeles en nuestra imagen por 100?
# ESTO SE LOGRA MEDIANTE LA CONSTRUCCION DE UNA MATRIZ (CON SOLO VALORES 1) Y MULTIPLICAR CADA VALOR POR 100???
# DESPUES SOLO AGREGAMOS LA IMAGEN PARA OBTENER UN TONO MAS BRILLANTE ???????? ES VERDAD????
# COMO OBTENGO UNA IMAGEN MAS BRILLANTE??????

# By applying add we make the image brighter.
# We are building a NumPy array using the image shape as the argument for the number of rows and columns our
# new numpy array should contain
M = np.ones(image.shape, dtype = "uint8") * 100

print(image[0,0])
# Then we use openCV to add that Numpy array to our original image, and what this will do
# is that it will add 100 to each of the pixels in the original image
# Meaning if pixel at position 0,0 had as values (100,50,70) after the cv2.add 
# That same pixel will hold the values (200,150,170)

added = cv2.add(image, M)
print(added[0,0])
cv2.imshow("VALOR ADICIONADO", added)

# SUCEDE LO MISMO SI RESTAMOS 50?????? OBTENEMOS UNA IMAGEN MAS OSCURA
# COMO FUNCIONA ??????

# When we subtract from an image we get a darker image.
# The subtraction works just as the addition but instead of adding the value to each position,
# we are going to subtract that value from each pixel's rgb values
# Meaning if pixel at position 0,0 had as values (100,100,70) after the cv2.subtract 
# That same pixel will hold the values (50,50,20)

M = np.ones(image.shape, dtype = "uint8") * 50
print(image[0,0])
subtracted = cv2.subtract(image, M)
print(subtract[0,0])
cv2.imshow("VALOR RESTADO", subtracted)
cv2.waitKey(0)