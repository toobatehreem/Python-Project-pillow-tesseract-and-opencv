import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

image = Image.open('text.png')
# image.show()

print(dir(pytesseract))

print(help(pytesseract.image_to_string))
print(help(Image.Image.resize))

import inspect

src = inspect.getsource(pytesseract.image_to_string)
print(src)

text = pytesseract.image_to_string(image)
print(text)
print('\n')

noisy_img = Image.open('noisy1.png')
text1 = pytesseract.image_to_string(noisy_img)
print(text1)
print('\n')

#changing the size of the image

basewidth =600
wpercent = (basewidth/float(noisy_img.size[0]))
hsize = int((float(noisy_img.size[1])* float(wpercent)))
noisy_img = noisy_img.resize((basewidth,hsize), Image.ANTIALIAS)

noisy_img.save('resized_noisy_img.png')

resized = Image.open('resized_noisy_img.png')
# resized.show()
text1 = pytesseract.image_to_string(resized)
print(text1)

print('\n')

noisy_img = noisy_img.convert('L')
noisy_img.save('grayscale_noise.jpg')
grayscale_noise = Image.open('grayscale_noise.jpg')
# grayscale_noise.show()
text1 = pytesseract.image_to_string(grayscale_noise)
print(text1)

blackandwhite_noise = Image.open('noisy1.png').convert('1') #binarization
blackandwhite_noise.save('blackandwhite_noise.png')
# blackandwhite_noise.show()

def binarize(image_to_transform, threshold):
    output_image = image_to_transform.convert('L')

    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y)) < threshold:
                output_image.putpixel((x,y), 0)
            else:
                output_image.putpixel((x,y), 255)

    return output_image

for thresh in range(0, 257, 64):
    print("Trying with threshold: " + str(thresh)) #threshold 0 giving a white image and 256 giving a black image
    new_image = binarize(Image.open('noisy1.png'), thresh)
    # new_image.show()

    print(pytesseract.image_to_string(new_image))
    print('\n')

store_image = Image.open('store.jpg')
store_image.show()

store_text = pytesseract.image_to_string(store_image)
print(store_text)

bounding_box = (50,50,400,170)
cropped_image = store_image.crop(bounding_box)
cropped_image.show()

cropped_text = pytesseract.image_to_string(cropped_image)
print(cropped_text)

new_size = (cropped_image.width*10, cropped_image.height*10)
new_image = cropped_image.resize(new_size, Image.BICUBIC)
new_image.show()

new_text = pytesseract.image_to_string(new_image)
print(new_text)