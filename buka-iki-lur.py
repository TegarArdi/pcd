# iki ora masuk laporan

from PIL import Image


pic = Image.open('gambar-biasa.jpg').convert('L')
pic.save('gambar-grayscale.jpg')

# ubah gambar rgb dkk. menjadi grayscale untuk pengolahan citra digital