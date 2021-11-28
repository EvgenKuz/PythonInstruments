from PIL import Image
import numpy as np


def convert_image_to_pixelart(image, chunk_size=10, grey_gradation=5):
    arr = np.array(image)
    gradient = 255 // grey_gradation

    for x in range(0, arr.shape[0], chunk_size):
        for y in range(0, arr.shape[1], chunk_size):
            grey = arr[x:x+chunk_size, y:y+chunk_size].sum() / 3
            grey = grey / chunk_size ** 2 // gradient * gradient

            arr[x:x+chunk_size, y:y+chunk_size] = grey

    return arr


image_name = "img2.jpg"
mosaic = 10
gradation = 5

img = Image.open(image_name)
res = Image.fromarray(convert_image_to_pixelart(img, mosaic, gradation))
res.save('results/mine_without_input.jpg')
