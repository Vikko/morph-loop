from morph import Morph

import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

class PCAMorph(Morph):
    """
    Variant on the simple morphing that uses eigenvectors for a smooth transition.
    Results are not satifactory.
    """
    data = None
    pca = None
    dim = None

    def __init__(self, data):
        """
        Initializer that calculates a PCA on all data.

        :param data: array of all images [n][x][y][c]
        """
        self.dim = (data.shape[1], data.shape[2], data.shape[3])
        images = pd.DataFrame([])
        for i in range(0,data.shape[0]):
            img = pd.Series(data[i].flatten(),name=(i+1))
            images = images._append(img)

        self.pca = PCA(n_components=(data.shape[0]-1))
        self.pca.fit(images)
        self.data = self.pca.transform(images)

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
        component = (1.0-x)*src+x*dst
        img = self.pca.inverse_transform(component)
        img = img.reshape(self.dim)
        return img
