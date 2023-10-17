import os
import numpy as np
import cv2 as cv

class ImageTools:
    """
    Class that wraps all image related tooling, passes on numpy arrays to the other modules
    """
    data = None

    def __init__(self):
        """
        Initializes class
        """
        pass

    @classmethod
    def get_images(cls, force=False) -> np.array:
        """
        Reads all images. Requires all images to be of the same dimensions and color channels

        :return: numpy array [n][x][y][c] (where n is the total amount of images)
        """
        if force:
            cls.data = None
        if cls.data == None:
            data_array = cls.read_files('../data')
            cls.data = np.array(data_array)
        return cls.data

    @classmethod
    def read_files(cls,dir) -> [np.array]:
        """
        Datareader for the folder.

        :param dir: relative directory in which the images are located
        :return: array of numpy arrays
        """
        images = []
        for file in os.listdir(dir):
            im = cv.imread(dir+'/'+file)
            if file is not None:
                images.append(im)
        return images

    @classmethod
    def showimg(cls, data, delay=0):
        """
        Display image in a window.

        :param data: nparray with the image [x][y][c] scaled as uint8, maxvalue 255
        :param delay: Amount of milliseconds to hold the image before moving on. 0 for indefinately.
        """
        cv.imshow("Show Image", data/255)
        cv.waitKey(delay)