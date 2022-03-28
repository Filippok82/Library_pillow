# обрезка изображения

# from PIL import Image

# img = Image.open('taksa.jpg')
# cropped = img.crop((0, 0, 300, 400))
# cropped.save('cropped_taksa.jpg')
# img = Image.open('cropped_taksa.jpg')
# img.show()


#_____________________________________________


# Изменения размера изображения

# from PIL import Image
# img = Image.open('taksa.jpg')
# img = img.resize((170, 100), Image.ANTIALIAS)
# img.save('test_taksa.jpg')
# img = Image.open('test_taksa.jpg')
# img.show()

#______________________________________

# Изменение ширины с учетом пропорций для новой высоты изображения

# from PIL import Image
 
# tatras = Image.open("taksa.jpg")
 
# width, height = tatras.size
# new_width  = 580 # ширина
# new_height = int(new_width * height / width)
 
# tatras = tatras.resize((new_width, new_height), Image.ANTIALIAS)
# tatras.show()

#___________________________________________
# Изменение высоты изображения, пропорционально обновляем и ширину

from PIL import Image
 
tatras = Image.open("taksa.jpg")
 
width, height = tatras.size
new_height = 680 # Высота
new_width  = int(new_height * width / height)
 
tatras = tatras.resize((new_width, new_height), Image.ANTIALIAS)
tatras.show()