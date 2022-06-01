# Importing cv2 library (OpenCV's python implementation)
import cv2

#Load an image and display basic information about the image width, height and channels
# cv2.imread() function is used to load an image.
# cv2.imread() function takes the path of the image as the argument.
# cv2.imread() function returns the image loaded as an array of numbers.
# cv2.imread() function returns a numpy array.
image = cv2.imread("./images/grand_canyon.png")

# We can access the image's width, height and channels using the shape attribute.
# The shape attribute returns a tuple of the image's dimensions.
# The first element of the tuple is the number of rows, the second element is the number of columns, and the third element is the number of channels.
print(image.shape);
# Meaning of the elements of the tuple:
# image.shape[0] = number of width
# image.shape[1] = number of height
# image.shape[2] = number of channels
print("width: {w} pixels".format(w=image.shape[1]))
print("height: {h}  pixels".format(h=image.shape[0]))
print("channels: {c}".format(c=image.shape[2]))

# cv2.imwrite() function is used to save an image.
# cv2.imwrite() function takes the path of the image as the first argument and the image as the second argument.
# cv2.imwrite() automatically manages the conversion of the image to the correct format.
# cv2.imwrite("./images/Imagen3.jpg", image)

# tarea : pida por teclado un nombre y guarde la imagen con el nombre solicitado
print("Enter a name for the image")
name = input()
cv2.imwrite("./images/" + name + ".jpg", image)

# cv2.imshow() function is used to display an image.
# cv2.imshow() function takes the name of the window as the first argument and the image as the second argument.
# cv2.imshow() function returns None.
cv2.imshow("Image", image)

# cv2.waitKey() function is used to display an image and wait for a key press.
# cv2.waitKey() function takes the time in milliseconds as the argument.
# cv2.waitKey() function returns the code of the key that was pressed.
cv2.waitKey(0)