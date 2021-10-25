from PIL import Image

pic = Image.open('grayscale.jpg')

# untuk menyimpan pixel gambar asli
pixels = []
for x in range(pic.width):
  temp = []
  for y in range(pic.height):
    value = pic.getpixel((x, y))
    temp.append(value)
  
  pixels.append(temp)


# rotasikan pixel 90 derajat
rotated = list(zip(*pixels))[::-1]
# buat gambar baru dengan ukuran panjang
# dan lebar dibalik dari gambar asli
newPic = Image.new(mode='L', size=(pic.height, pic.width))

# isi gambar baru dengan pixel yang dirotasikan
for x in range(newPic.width):
  for y in range(newPic.height):
    value = rotated[x][y]
    newPic.putpixel((x, y), value)

newPic.save('rotated-90.jpg')