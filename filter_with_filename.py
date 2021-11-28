"""
Применяет фильтр пикселизации и серого цвета к
изображению.

Проверим, что создаётся изображение
>>> import os.path
>>> os.path.exists("results/mine_without_input.jpg")
True
"""
from PIL import Image
import filter

image_name = "img2.jpg"
mosaic = 10
gradation = 5

img = Image.open(image_name)
res = Image.fromarray(filter.convert_image_to_pixelart(img, mosaic, gradation))
res.save('results/mine_without_input.jpg')
