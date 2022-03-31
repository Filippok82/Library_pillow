# Рисование объектов 

# from PIL import Image, ImageDraw
 
# # Пустой желтый фон.
# im = Image.new('RGB', (500, 300), (219, 193, 27))
# draw = ImageDraw.Draw(im)

# # Рисуем красный эллипс с черной оконтовкой.
# draw.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))
 
# # Рисуем синий прямоугольник с белой оконтовкой.
# draw.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))
 
# # Рисуем розовую линию с шириной в 10 пиксель.
# draw.line((350, 200, 450, 100), fill='pink', width=10)
 
# im.save('test2.jpg', quality=95)
# im.show()

#______________________________________________________________________________

# Рисование смайлика

# from PIL import Image, ImageDraw
 
# image = Image.new('RGB', (90, 90), 'white')
# draw = ImageDraw.Draw(image)
 
# draw.ellipse((0, 0, 90, 90), 'yellow', 'blue')
# draw.ellipse((25, 20, 35, 30), 'yellow', 'blue')
# draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
# draw.arc((20, 40, 70, 70), 0, 180, 0)
# image.save('test3.jpg')
# image.show()

#____________________________________________________________________
#Рисование линии, многоугольника и точки

# from PIL import Image, ImageDraw
 
# # Пустой желтый фон.
# im = Image.new('RGB', (500, 300), (219, 193, 27))
# draw = ImageDraw.Draw(im)
 
# # Три черные линии в шириной в 1 пиксель.
# draw.line(
#     xy=(
#         (30, 200),
#         (130, 100),
#         (80, 50)
#     ), fill='black')
 
# # Три красные линии с размером в 5 пикселей.
# draw.line(
#     xy=(
#         (80, 200),
#         (180, 100),
#         (130, 50)
#     ), fill='red', width=10)
 
# # Имея три точки и связь между ними, у нас получится синий треугольник.
# draw.polygon(
#     xy=(
#         (200, 200),
#         (300, 100),
#         (250, 50)
#     ), fill='blue', outline=(0, 0, 0)
# )
 
# # Рисуем три точки.
# draw.point(
#     xy=(
#         (350, 200),
#         (450, 100),
#         (400, 50)
#     ), fill='black'
# )
 
# im.save('test3.jpg', quality=95)
# im.show()

#________________________________________________________________

# Рисование дуги, хорды и пирога
# from PIL import Image, ImageDraw
 
# # Пустой желтый фон.
# im = Image.new('RGB', (610, 240), (219, 193, 27))
# draw = ImageDraw.Draw(im)
 
# # Рисуем дугу.
# draw.arc(
#     xy=(25, 50, 175, 200),
#     start=30, end=270,
#     fill='red'
# )
 
# # Рисуем хорду.
# draw.chord(
#     xy=(225, 50, 375, 200),
#     start=30, end=270, fill=(255, 255, 0),
#     outline=(0, 0, 0)
# )
 
# # Рисуем "кусок пирога".
# draw.pieslice(
#     xy=(425, 50, 575, 200),
#     start=30, end=270, fill=(255, 255, 0),
#     outline=(0, 0, 0)
# )
# im.save('test4.jpg')
# im.show()

# ______________________________________________

# Рисование поверх изображения
from PIL import Image, ImageDraw
 
im = Image.open('taksa.jpg')
draw = ImageDraw.Draw(im)
 
draw.pieslice(
    xy=(15, 50, 140, 175),
    start=30, end=330,
    fill='red'
)
 
im.save('taksa_with_pieslice.jpg', quality=95)
im.show()