import os
import cv2
import numpy as np


class ImageLoader:
    def __init__(self, root="./"):
        self.root = root

    def load(self, filename):
        path = os.path.join(self.root, filename)

        image = cv2.imread(path, cv2.IMREAD_COLOR).copy().astype(np.float32)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image /= 255.0

        return image
