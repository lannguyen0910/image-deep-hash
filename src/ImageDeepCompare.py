import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import pairwise_distances
from src.ImageLoader import ImageLoader
from src.ModelFactory import ModelFactory


class ImageDeepCompare:
    def __init__(self, weight="VGG16", root="./", image_size=(224, 224, 3)):
        self.root = root
        self.image_size = image_size
        self.imageLoader = ImageLoader.ImageLoader(self.root, self.image_size)
        self.model_factory = ModelFactory.ModelFactory()

        self.image1 = np.zeros(self.image_size)
        self.image2 = np.zeros(self.image_size)

        self.model = self.model_factory.order(name=weight, input_shape=self.image_size, classes=2048)

    def compare(self, path1, path2, metric="euclidean"):
        self.image1 = self.imageLoader.load(path1)
        self.image2 = self.imageLoader.load(path2)

        predict1 = self.model.predict(np.array([self.image1]))
        predict2 = self.model.predict(np.array([self.image2]))
        return pairwise_distances(predict1, predict2, metric=metric)[0][0]

    def plot(self):
        f, axs = plt.subplots(1, 2)
        axs[0].imshow(self.image1)
        axs[1].imshow(self.image2)
        plt.show()
