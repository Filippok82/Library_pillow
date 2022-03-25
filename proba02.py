# обрезка изображения

# from PIL import Image

# img = Image.open('taksa.jpg')
# cropped = img.crop((0, 0, 300, 400))
# cropped.save('cropped_taksa.jpg')
# img = Image.open('cropped_taksa.jpg')
# img.show()


#_____________________________________________


# Изменения размера изображения

from PIL import Image
img = Image.open('taksa.jpg')
img = img.resize((170, 100), Image.ANTIALIAS)
img.save('test_taksa.jpg')
img = Image.open('test_taksa.jpg')
img.show()