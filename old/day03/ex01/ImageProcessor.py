#! /usr/bin/python3

from matplotlib import image
from matplotlib import pyplot
import numpy
import matplotlib
import numpy

class ImageProcessor():
    
    @staticmethod
    def load(path):
        return image.imread(path)

    @staticmethod
    def display(array):
        pyplot.imshow(array)

arr = ImageProcessor.load("../assets/img.png")
ImageProcessor.display(arr)
