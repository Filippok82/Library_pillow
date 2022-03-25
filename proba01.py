from PIL import Image


# 
# image = Image.open('taksa.jpg') # Открываем изображение 
# image.show()
# print(im.format, im.size, im.mode) # # Просмотр формата изображения, размер, типа цветового пространства


im = Image.open("RGB.jpg") # Открываем изображение
im.show()
print(im.format)
r,g,b = im.split()          
histogram = im.histogram() # Просмотр значений RGB изображения
print(histogram)
