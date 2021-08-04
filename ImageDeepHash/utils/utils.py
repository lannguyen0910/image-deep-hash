import tensorflow as tf
from binascii import unhexlify


def long_to_bytes(val, endianness='big'):
    """
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]

    return s


def load_backbone(name="ResNet50", input_shape=(224, 224, 3), classes=128):
    if name == "Xception":
        return tf.keras.applications.Xception(include_top=False, weights=None, classes=classes,
                                              input_shape=input_shape, classifier_activation='sigmoid')
    if name == "VGG16":
        return tf.keras.applications.VGG16(include_top=False, weights=None, classes=classes,
                                           input_shape=input_shape, classifier_activation='sigmoid')
    if name == "VGG19":
        return tf.keras.applications.VGG19(include_top=False, weights=None, classes=classes,
                                           input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet50":
        return tf.keras.applications.ResNet50(include_top=False, weights=None, classes=classes,
                                              input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet101":
        return tf.keras.applications.ResNet101(include_top=False, weights=None, classes=classes,
                                               input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet152":
        return tf.keras.applications.ResNet152(include_top=False, weights=None, classes=classes,
                                               input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet50V2":
        return tf.keras.applications.ResNet50V2(include_top=False, weights=None, classes=classes,
                                                input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet101V2":
        return tf.keras.applications.ResNet101V2(include_top=False, weights=None, classes=classes,
                                                 input_shape=input_shape, classifier_activation='sigmoid')
    if name == "ResNet152V2":
        return tf.keras.applications.ResNet152V2(include_top=False, weights=None, classes=classes,
                                                 input_shape=input_shape, classifier_activation='sigmoid')
    return None
