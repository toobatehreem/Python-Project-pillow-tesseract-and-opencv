import cv2

img = cv2.imread('test.jpg',1)

face_cascade = cv2.CascadeClassifier('cascade.xml')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))

print(faces)
#[[218 203 171 171]] these are the cordinates of the face
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

#resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))

cv2.imshow('Gray', img)
cv2.waitKey(0)
