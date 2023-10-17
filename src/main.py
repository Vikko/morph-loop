from img_tools import ImageTools
from morph import Morph
from pca import PCAMorph

import math
import numpy as np

class Main:
    def __init__(self):
        self.data = ImageTools().get_images()
        self.morpher = Morph(self.data)

    def morph_data(self, src, dst, x):
        return self.morpher.transition(src, dst, x)

    def showimg(self, img, delay=40):
        ImageTools.showimg(img, delay)

    def data_length(self):
        return self.data.shape[0]

if __name__ == "__main__":
    proc = Main()
    n = proc.data_length()
    for i in range(1,n-1):
        fps = 24.0
        for x in np.arange(0, 1, 1.0/fps):
            img = proc.morph_data(i-1,i,x)
            proc.showimg(img, math.floor(1000/fps))



