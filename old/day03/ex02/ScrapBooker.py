#! /usr/bin/python3

import numpy as np
import sys
from matplotlib import image as mImg
from matplotlib import pyplot as pPlot
class ScrapBooker():
    @staticmethod
    def crop(array, dimensions, position = (0, 0)):
        if dimensions[0] + position[0] > array.shape[0] or dimensions[1] + position[1] > array.shape[1]:
            exit("Error: given dimensions are too big")
        return array[position[0]:position[0]+dimensions[0],position[1]:position[1]+dimensions[1]]

    @staticmethod
    def thin(array, n, axis):
        pass

    @staticmethod
    def juxtapose(array, n, axis):
        pass
    
    @staticmethod
    def mosaic(array,dimensions):
        pass

arr = mImg.imread('../assets/img.png')
src = ScrapBooker()
arr2 = src.crop(arr, (200, 200), (50, 50))
pPlot.imshow(arr2)
