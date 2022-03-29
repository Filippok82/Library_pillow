# Загрузка изображени через URL

from PIL import Image
import requests  
import sys
 
url = 'https://i.pinimg.com/736x/0d/cb/de/0dcbde883a8c9c6ab115172f4dc6cf83.jpg'
 
try:
    resp = requests.get(url, stream=True).raw # Изображение читается как данные raw.
except requests.exceptions.RequestException as e:  
    sys.exit(1)
 
try:
    img = Image.open(resp) # Картинка создается из ответного объекта response.
except IOError:
    print("Unable to open image")
    sys.exit(1)
 
img.save('karlic.jpg', 'jpeg')
img = Image.open("karlic.jpg") # Открываем изображение
img.show()

#__________________________________________________________
# Черно-белое изображение

# from PIL import Image
# import sys
 
# try:
#     tatras = Image.open("taksa.jpg")
# except IOError: # Обработка исключений
#     print("Unable to load image")
#     sys.exit(1)
    
# grayscale = tatras.convert('L') # Программа читает изображение и трансформирует его в черно-белое.
# grayscale.show()