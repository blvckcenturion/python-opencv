import cv2
#import numpy
# Cesar Suarez
# Computacion Grafica y Robotica
# comente y explique que hacen las siguientes lineas de codigo?
# 7, 8, 9, 10, 11

# 7. We define a new function called detectarRostro and we pass img as a parameter
def detectarRostro(img):
    
    # 8. We define gray and set its value to the result of converting the img to gray scale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 9. Loading the required haar-cascade XML classifier file
    cara_cascada = cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")
    # 10. Basically the same thing as line 8
    grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 11.  Applying the face detection method on the grayscale image
    rostro = cara_cascada.detectMultiScale(grises, 1.3, 5)
    # 12. Iterating through rectangles of detected faces
    for (x,y,w,h) in rostro:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,128),2)
    return img
camara = cv2.VideoCapture(0)
while(True):
    ret, frame = camara.read()
    cara = detectarRostro(frame)
    cv2.imshow('Haar', cara)
    #cv2.imshow('Imagen', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camara.release()
cv2.destroyAllWindows()