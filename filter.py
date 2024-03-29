from PIL import Image
import numpy as np


def convert_image_to_pixelart(image, chunk_size=10, grey_gradation=5):
    """Пикселезирует изображание и делает его серым.
    Принимает объект изображение класса Image из
    библиотеки Pillow,
    возвращает array из NumPy.

    Проверим, что возвращаемый массив можно преобразовать в
    изображение.
    >>> (convert_image_to_pixelart(Image.open("img2.jpg")) < 256).all()
    True"""
    arr = np.array(image)
    gradient = 255 // grey_gradation

    for x in range(0, arr.shape[0], chunk_size):
        for y in range(0, arr.shape[1], chunk_size):
            grey = arr[x:x+chunk_size, y:y+chunk_size].sum() / 3
            grey = grey / chunk_size ** 2 // gradient * gradient

            arr[x:x+chunk_size, y:y+chunk_size] = grey

    return arr


image_name = input("Введите название файла изображения:")

mosaic = input("Введите размер мозаики(или нажмите Ввод для значения по-умолчанию = 10):")
mosaic = int(mosaic) if mosaic else 10

gradation = input("Введите шаг градации(или нажмите Ввод для значения по-умолчанию = 5):")
gradation = int(gradation) if gradation else 5

img = Image.open(image_name)
res = Image.fromarray(convert_image_to_pixelart(img, mosaic, gradation))
res.save('results/mine_with_input.jpg')

print("Получившееся изображение сохранено как results/mine_with_input.jpg")
