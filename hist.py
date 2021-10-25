import cv2
import numpy as np


pic = cv2.imread('to_equalize.jpg', 0)
row, col = pic.shape[:2]


def df(img):
  val = [0] * 256
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      val[img[i, j]] += 1
  
  return val


def cdf(hist):
  cdf = [0] * len(hist)
  cdf[0] = hist[0]
  for i in range(1, len(hist)):
    cdf[i] = cdf[i - 1] + hist[i]
  
  cdf = [ele * 255 / cdf[-1] for ele in cdf]
  return cdf


def equalize(img):
  my_cdf = cdf(df(img))
  equalized = np.interp(img, range(0, 256), my_cdf)
  return equalized


eq = equalize(pic)
cv2.imwrite('equalized2.jpg', eq)