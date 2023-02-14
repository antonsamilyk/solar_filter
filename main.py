from PIL import Image
import numpy
from time import sleep

try:
    img = Image.open('cameraman.tif')
except FileNotFoundError:
    print("Зображення не знайдено!")


def solar(img):
    newimarray = []
    imgarray = numpy.array(img)
    x_max = imgarray.max()
    for i in range(len(imgarray)):
        temp = []
        for j in range(len(imgarray[i])):

            y_i_j = imgarray[i][j]*(x_max - imgarray[i][j])
            temp.append(y_i_j)

        newimarray.append(temp)
    np_newarr = numpy.array(newimarray, dtype=numpy.uint8)
    newIm = Image.fromarray(np_newarr)
    newIm.show()
    #print(np_newarr)
    return newIm


def lin_contrast(img, y_min, y_max):
    newimarray = []
    imgarray = numpy.array(img)
    y_min = y_min
    y_max = y_max
    x_min = imgarray.min()
    x_max = imgarray.max()
    for i in range(len(imgarray)):
        temp = []
        for j in range(len(imgarray[i])):

            y_i_j = ((imgarray[i][j] - x_min) / (x_max - x_min))*(y_max - y_min) + y_min
            temp.append(y_i_j)

        newimarray.append(temp)
    np_newarr = numpy.array(newimarray, dtype=numpy.uint8)
    newIm = Image.fromarray(np_newarr)
    newIm.show()
    print(x_min, x_max)
    print(np_newarr.min(), np_newarr.max())


img.show()
sleep(3)

img_solar = solar(img)
sleep(3)

lin_contrast(img_solar, 0, 255)