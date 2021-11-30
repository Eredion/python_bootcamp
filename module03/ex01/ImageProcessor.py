#!/usr/bin/env python

import numpy as np
from PIL import Image as Img

class ImageProcessor:
    def load(path):
        try :
            img = Img.open(path)
            print("Loading image of dimensions {} x {}".format(img.size[0], img.size[1]))
            return np.asarray(img)
        except:
            print("Error: Could not open file")

    def display(array):
        try:
            img = Img.fromarray(array)
            img.show()
        except:
            print("Error: Could not display image")
        pass


if __name__ == '__main__':
    arr = ImageProcessor.load('../resources/42AI.png')
    ImageProcessor.display(arr)
