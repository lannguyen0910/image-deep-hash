import os
import cv2
import numpy as np


class ImageLoader:
    def __init__(self, root="./", image_size=(224, 224, 3)):
        self.root = root
        self.image_size = image_size

    def load(self, filename):
        path = os.path.join(self.root, filename)

        image = cv2.imread(path, cv2.IMREAD_COLOR).copy().astype(np.float32)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image = cv2.resize(image, (self.image_size[0], self.image_size[1]))
        image /= 255.0

        return image
