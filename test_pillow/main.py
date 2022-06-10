from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests

# img = Image.open('avotar.jpg')

# img.show()
# print(img.size)
# print(img.format)
# print(img.mode)
# print(img.histogram)

# img.thumbnail((133, 452))
# img.save('mini_avotar.jpg')
# print(img.size)
# img.show()
# crop_img = img.crop((200, 300, 400, 500))
# crop_img.save('crop_avotar.jpg')
# crop_img.show()

# rotate_img = img.rotate(90)
# rotate_img.save('rotate_avotar.jpg')
# rotate_img.show()

# blur_img = img.filter(ImageFilter.BLUR)
# blur_img.save('blur_avatar.jpg')
# blur_img.show()

# contur_img = img.filter(ImageFilter.CONTOUR)
# contur_img.save('contur_avotar.jpg')
# contur_img.show()

# img = Image.new('RGBA', (600, 1000), 'gray')
# idrow = ImageDraw.Draw(img)
# headline = ImageFont.truetype('arial.ttf', size=50, )
#
# idrow.rectangle((550, 800, 50, 250), fill='green')
# idrow.text((150, 500), 'Hello World!', font=headline)
#
# img.save('my_draw.png')
# img.show()

# url = input('::::> ')
# response = requests.get(url, stream=True).raw
# img = Image.open(response)
#
# img.save('daunlowdied.jpg', 'jpeg')
# img.show()
