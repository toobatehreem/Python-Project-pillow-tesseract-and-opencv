import cv2 as cv

face_cascade = cv.CascadeClassifier('cascade.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

image = cv.imread('test.jpg')
cv.imshow('Output', image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

faces = face_cascade.detectMultiScale(gray)
print(faces)
print(faces.tolist()[0]) #x,y,w,h x and y makes the upper left point

from PIL import Image

pil_image = Image.fromarray(gray, 'L')

from PIL import ImageDraw

drawing = ImageDraw.Draw(pil_image)

for x,y,w,h in faces:
    drawing.rectangle((x,y,x+w, y+h), outline='white')

pil_image.show()

def show_rects(faces):
    pil_image = Image.open('test.jpg').convert('RGB')
    drawing = ImageDraw.Draw(pil_image)
    for x, y, w, h in faces:
        drawing.rectangle((x, y, x + w, y + h), outline='black', width=10)
    pil_image.show()

cv_img_bin = cv.threshold(image, 120, 255, cv.THRESH_BINARY)[1]
faces = face_cascade.detectMultiScale(cv_img_bin)
show_rects(faces)

faces = face_cascade.detectMultiScale(image, 1.05)
show_rects(faces)

faces = face_cascade.detectMultiScale(image, 1.15)
show_rects(faces)

faces = face_cascade.detectMultiScale(image, 1.25)
show_rects(faces)

cv.waitKey(20)
cv.destroyAllWindows()
