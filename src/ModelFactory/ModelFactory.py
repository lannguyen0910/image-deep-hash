import os
import tensorflow as tf
from src.utils.utils import *


class ModelFactory:
    def __init__(self):
        self.factory = {
            "Xception",
            "VGG16",
            "VGG19",
            "ResNet50",
            "ResNet101",
            "ResNet152",
            "ResNet50V2",
            "ResNet101V2",
            "ResNet152V2",
            "InceptionV3",
            "InceptionResNetV2",
            "MobileNet",
            "MobileNetV2",
            "DenseNet121",
            "DenseNet169",
            "DenseNet201",
            "NASNetMobile",
            "NASNetLarge",
            "EfficientNetB0",
            "EfficientNetB1",
            "EfficientNetB2",
            "EfficientNetB3",
            "EfficientNetB4",
            "EfficientNetB5",
            "EfficientNetB6",
            "EfficientNetB7",
        }
        self.flexible_model = {}

    def order(self, name="ResNet50", input_shape=(224, 224, 3), classes=128, format=None):
        if name in self.flexible_model:
            if self.flexible_model[name].endswith(".py"):
                return self.load_message_broker_model(self.flexible_model[name])
            else:
                return self.load_model_from_path(self.flexible_model[name])
        elif name in self.factory:
            return load_backbone(name="ResNet50", input_shape=input_shape, classes=classes)
        elif os.path.isfile(name):
            self.flexible_model["custom_model" +
                                str(len(self.flexible_model))] = name
            if name.endswith(".py"):
                return self.load_message_broker_model(name)
            else:
                return self.load_model_from_path(name)
        return False

    @staticmethod
    def load_model_from_path(path):
        return tf.keras.models.load_model(path, compile=False)

    @staticmethod
    def load_message_broker_model(path):
        result = {}
        exec(open(path).read(), result)
        return result["model"]
