# генерация пустого изображения

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'pink')
img.save('test.jpg')
img = Image.open('test.jpg')
# img.show()

# Дорисуем в розовом квадрате круг

idraw = ImageDraw.Draw(img)
# idraw.rectangle((1, 1, 100, 100), fill='white')# белый квадрат в в розовом квадрате
idraw.ellipse((20, 20, 90, 90), fill='gray') # серый круг в розом 
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()