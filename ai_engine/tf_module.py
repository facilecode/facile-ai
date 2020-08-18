import tensorflow as tf 
import tensorflow.keras as K
import tensorflow.keras.applications as models
import tensorflow.keras.activations as activations
import tensorflow.keras.layers as layers
import cv2

class Trainer:

    named_layers = {
        # activations
        "relu": activations.relu,
        "lrelu": activations.LeakyReLU,
        "sigmoid": activations.Sigmoid,
        "lsigmoid": activations.LogSigmoid,
        "softmax": activations.Softmax,
        "lsoftmax": activations.LogSoftmax,
        "tanh": activations.Tanh,
        # linear
        "linear": layers.Dense,
        # flatten
        "flatten": layers.Flatten,
        # conv
        "conv2d": layers.Conv2D,
        #  norm
        "batch_norm": layers.BatchNormalization,
        "layer_norm": layers.LayerNormalization,
        # dropout
        "dropout": layers.Dropout,
        #"dropout2d": layers.Dropout2d,
        # pooling
        "maxpool_2d": layers.MaxPool2D,
        'gmaxpool_2d': layers.GlobalMaxPool2D,
        "avgpool_2d": layers.AveragePooling2D,
        "global_avgpool_2d": layers.GlobalAveragePooling2D
    }

    named_models = {
        "mobilenet_v2": models.MobileNetV2(),
        "resnet_50": models.resnet50(),
        "resnet_50_v2": models.ResNet50V2(),
        "inception_v3": models.inception_v3()
    }