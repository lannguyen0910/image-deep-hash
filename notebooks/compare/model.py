import numpy as np
import tensorflow as tf


class MyModel:
    def __init__(self):
        self.SAVED_MODEL_DIR = 'glr_model'
        self.DELG_MODEL = tf.saved_model.load(self.SAVED_MODEL_DIR)
        self.DELG_IMAGE_SCALES_TENSOR = tf.convert_to_tensor([0.70710677, 1.0, 1.4142135])
        self.DELG_SCORE_THRESHOLD_TENSOR = tf.constant(175.)
        self.DELG_INPUT_TENSOR_NAMES = ['input_image:0', 'input_scales:0', 'input_abs_thres:0']

        # Global feature extraction:
        self.GLOBAL_FEATURE_EXTRACTION_FN = self.DELG_MODEL.prune(
            self.DELG_INPUT_TENSOR_NAMES,
            ['global_descriptors:0'])

    def predict(self, image_tensor):
        features = self.GLOBAL_FEATURE_EXTRACTION_FN(image_tensor,
                                                     self.DELG_IMAGE_SCALES_TENSOR,
                                                     self.DELG_SCORE_THRESHOLD_TENSOR)

        return np.array([tf.nn.l2_normalize(
            tf.reduce_sum(features[0], axis=0, name='sum_pooling'),
            axis=0,
            name='final_l2_normalization').numpy()])


model = MyModel()
