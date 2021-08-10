import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from ImageDeepHash.utils.utils import *
from ImageDeepHash.ImageLoader import ImageLoader
from ImageDeepHash.ModelFactory import ModelFactory


class ImageDeepHash:
    def __init__(self, weight="VGG16", hex_len=16, root="./", image_size=(224, 224, 3)):
        self.hex_len = hex_len
        self.root = root
        self.image_size = image_size
        self.imageLoader = ImageLoader.ImageLoader(self.root, self.image_size)
        self.model_factory = ModelFactory.ModelFactory()
        self.image = np.zeros(self.image_size)
        self.list_digest = [0]*self.hex_len*8

        self.model = self.model_factory.order(name=weight, input_shape=self.image_size, classes=self.hex_len*8)
        self.continuous_layer = tf.keras.Sequential(
            tf.keras.layers.Dense(self.hex_len*8, activation="sigmoid")
        )

    def reset(self):
        self.list_digest = [0] * self.hex_len * 8

    def hash(self, path):
        self.image = self.imageLoader.load(path)
        predict = self.model.predict(np.array([self.image]))[0]
        predict = (predict > 0.5).astype(np.int).tolist()
        predict = self.continuous_layer.predict(np.array([self.list_digest + predict]))[0]
        self.list_digest = (predict > 0.5).astype(np.int).tolist()

    def digest(self):
        bin_str = "".join(map(str, self.list_digest))
        return long_to_bytes(int(bin_str, 2))

    def hexdigest(self):
        bin_str = "".join(map(str, self.list_digest))
        return hex(int(bin_str, 2))

    def plot(self):
        plt.imshow(self.image)
        plt.show()
