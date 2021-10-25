from PIL import Image

pic = Image.open('grayscale.jpg')

for x in range(pic.width):
  for y in range(pic.height):
    coordinat = (x, y)
    if pic.getpixel(coordinat) > 127:  # treshold
      result = 0  # hitam
    else:
      result = 255  # putih
    
    pic.putpixel(coordinat, result)

pic.save('tresholding.jpg')