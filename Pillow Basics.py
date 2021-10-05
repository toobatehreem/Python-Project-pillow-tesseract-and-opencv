from PIL import Image

print(help(Image))
im = Image.new(mode="RGB", size=(200, 200),  color = (153, 153, 255))
# im.show()

#when we want to pass a reference to a function and not run the function, we use it without parentheses

print(help(Image.open))

file = 'maxresdefault.jpg'
image = Image.open(file)
# image.show()
print(image)

import inspect

print("The type of the image is: " + str(type(image)))
inspect.getmro(type(image))

from IPython.display import display #for displaying image in jupyter notebook
display(image)

image.save('newmaxresdefault.png')
new_image = Image.open('newmaxresdefault.png')
# new_image.show()

inspect.getmro(type(new_image))

from PIL import ImageFilter
#blurring an image
image = image.convert('RGB')
blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.show()

print("{}x{}".format(image.width, image.height)) #width is x-axis and height is y-axis

cropped = image.crop((50,0,150,150)) #(left, upper, right, lower)- tuple
# cropped.show()

from PIL import ImageDraw

drawing_object = ImageDraw.Draw(image)
drawing_object.rectangle((50,0,190,150), fill=None, outline='red')
# image.show()

newsize = (300, 300)
image = image.resize(newsize)

from PIL import ImageEnhance
import cv2
import numpy as np

print(image.size)
enhancer = ImageEnhance.Brightness(image)
images = []

for i in range(10):
    images.append(enhancer.enhance(i/10))

Hori = np.concatenate(([images[i] for i in range(10)]), axis=1)

cv2.imshow('HORIZONTAL', Hori)
cv2.waitKey(0)

first_image = images[0]
contact_sheet = Image.new(first_image.mode, (first_image.width, 10*first_image.height))

current_location = 0

for img in images:
    contact_sheet.paste(img, (0, current_location))
    current_location = current_location+300

contact_sheet = contact_sheet.resize((160,900))
contact_sheet.show()

contact_sheet_new = Image.new(first_image.mode, (first_image.width*3, first_image.height*3))

x = 0
y= 0

for img in images[1:]:
    contact_sheet_new.paste(img, (x,y))
    if x+first_image.width == contact_sheet_new.width:
        x=0
        y=y+first_image.height
    else:
        x = x+ first_image.width

contact_sheet_new = contact_sheet_new.resize(((int(contact_sheet_new.width/2)), int(contact_sheet_new.height/2)))
contact_sheet_new.show()




