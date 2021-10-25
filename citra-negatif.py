from PIL import Image

pic = Image.open('grayscale.jpg')

for x in range(pic.width):
  for y in range(pic.height):
    coordinat = (x, y)
    value = pic.getpixel(coordinat)
    result = 255 - value
    pic.putpixel(coordinat, result)

pic.save('citra-negatif.jpg')