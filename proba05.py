# Применение фильтров 

# from PIL import ImageFilter
# from PIL import Image
 
# image = Image.open('taksa.jpg')
# blurry_taksa = image.filter(ImageFilter.BLUR) # создает на его основе размытую картинку, используя ImageFilter.BLUR
# blurry_taksa.save('blurry_taksa.png') # сохраняет полученный результат на диск с помощью метода save() 
# img = Image.open('blurry_taksa.png')
# img.show()

#____________________________________________________________
# Увеличение резкости изображения 

from PIL import ImageFilter
from PIL import Image
 
image = Image.open('taksa.jpg')
sharp_taksa= image.filter(ImageFilter.SHARPEN)
sharp_taksa.save('sharp_taksa.png')
img = Image.open('sharp_taksa.png')
img.show()
