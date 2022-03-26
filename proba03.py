# from PIL import Image

# Поворот изображения

# img = Image.open('taksa.jpg')
# rotated = img.rotate(80)
# rotated.save('rotated_taksa.jpg')
# img = Image.open('rotated_taksa.jpg')
# img.show()

# ________________________________________

# Конвертация из jpg в png 

# img = Image.open('taksa.jpg')
# img.save('taksa_png.png', 'png')
# img.show()

#_________________________________

# Написание текста на изображении

from PIL import Image, ImageDraw, ImageFont
img = Image.open('taksa.jpg')
font = ImageFont.truetype("arial.ttf", size=50)
idraw = ImageDraw.Draw(img)
idraw.text((50, 50), 'Милый пёс', font=font, fill='#1C0606')
img.save('text_taksa.jpg')
img = Image.open('text_taksa.jpg')
img.show()