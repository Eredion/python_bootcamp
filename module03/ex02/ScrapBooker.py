#!/usr/bin/env python

import numpy as np

class ScrapBooker:
    def crop(array, dimensions, position=(0, 0)):
        # Crop the array to the given dimensions and position
        return array[position[0]:position[0]+dimensions[0], position[1]:position[1]+dimensions[1]]

    def thin(array, n, axis):
            if axis == 0:
                return array[:, ::n]
            elif axis == 1:
                return array[::n, :]

    def juxtapose(array, n, axis):
        pass

    def mosaic(array, dimensions):
        pass


if __name__ == '__main__':
    arr = np.array([['A','B','C', 'D', 'E', 'F','G','H'], ['A','B','C', 'D', 'E', 'F','G','H'], ['A','B','C', 'D', 'E', 'F','G','H']])
    print(ScrapBooker.crop(arr, (2, 2), (0, 2)))
    print(ScrapBooker.thin(arr, 2, 0))
