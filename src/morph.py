import numpy as np


class Morph:
    """
    Class that controls the morphing algorithm, takes in a data vector on initialisation for pre-processing
    """
    data = None

    def __init__(self, data):
        """
        :param data: array of all images [n][x][y][c]
        """
        self.data = data

    def transition(self, i_s, i_d, x) -> np.array:
        """
        Function to morph from a source to a destination image.

        :param i_s: index of the source image
        :param i_d: index of the destination image
        :param x: point of morphing, 0 fully source, 1 fully destination, 0.5 half way
        :return: nparray with the morphed image
        """
        src = self.data[i_s]
        dst = self.data[i_d]
        img = (1.0-x)*src+x*dst
        return img
