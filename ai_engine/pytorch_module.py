import torch
import torch.nn as nn
import torchvision.models as models
from PIL import Image
import cv2

class Trainer:

    named_layers = {      
        #activations
        "relu":"ok" ,
        # linear
        "linear": nn.Linear,
        # conv
        "conv_2d": nn.Conv2d,
        # batch norm
        "batch_norm": nn.BatchNorm2d,
        # dropout
        "dropout": nn.Dropout,
        "dropout_2d": nn.Dropout2d,
        # pooling
        "maxpool_2d": nn.MaxPool2d,
        'maxunpool_2d': nn.MaxUnpool2d,
        "avgpool_2d": nn.AvgPool2d,
        "adaptivemaxpool_2d": nn.AdaptiveAvgPool2d,
        "adaptiveavgpool_2d": nn.AdaptiveAvgPool2d
    }
    def __init__(self):

        self.named_layers = {
            # activations
            "relu": self.init_activation,
            "relu6": self.init_activation,
            "lrelu": self.init_activation,
            "sigmoid": self.init_activation,
            "lsigmoid": self.init_activation,
            "softmax": self.init_activation,
            "lsoftmax": self.init_activation,
            "tanh": self.init_activation,
            # linear
            "linear": self.init_linear,
            # dropout
            "dropout": self.init_droput,
            # conv 2d
            "conv_2d": self.init_conv2d,
            # pooling
            "maxpool_2d": self.init_maxpool_2d,
            "avgpool_2d": self.init_avgpool_2d,
            "adaptivemaxpool_2d": self.init_adaptive_maxpool_2d,
            "adaptiveavgpool_2d": self.init_adaptive_avgpool_2d
        }

        self.model = None
        self.base_model = None
        self.classifier = None
        self.custom_model = None
    
    def build_from_skratch(self, arch):

        layers = []
        for name, args in arch:
            
            layer = self.named_layers[name](name)

            layers.append(layer)
            layer = None
        
        self.model = nn.Sequential(nn.ModuleList(layers))

    """ init activations """
    def init_activation(self, name):

        if name == "relu":
            return nn.ReLU()
        
        if name == "relu6":
            return nn.ReLU6()
        
        if name == "lrelu":
            return nn.LeakyReLU()
        
        if name == "sigmoid":
            return nn.Sigmoid()
        
        if name == "lsigmoid":
            return nn.LogSigmoid()

        if name == "softmax":
            return nn.Softmax(dim=1)
        
        if name == "lsoftmax":
            return nn.LogSoftmax()
        
        if name == "tanh":
            return nn.Tanh()
    
    """ layers """
    def init_linear(self, ins, outs, bias):
        return nn.Linear(in_features=ins, out_features=outs, bias=bias)

    """ dropout """
    def init_droput(self, p):
        return nn.Dropout(p=p)
    
    """ conv 2d """
    def init_conv2d(self, ins, outs, kernel, stride=1, padding=0, dilation=1):
        return nn.Conv2d(in_channels=ins, 
                         out_channels=outs,
                         kernel_size=kernel,
                         stride=stride,
                         padding=padding,
                         dilation=dilation)
    
    """ pooling layers """
    def init_maxpool_2d(self, kernel_size, stride, padding, dilation):
        return nn.MaxPool2d(kernel_size=kernel_size,
                            stride=stride,
                            padding=padding,
                            dilation=dilation)
    
    def init_avgpool_2d(self, kernel_size, stride, padding):
        return nn.AvgPool2d(kernel_size=kernel_size,
                            stride=stride,
                            padding=padding)

    def init_adaptive_maxpool_2d(self, output_size):
        return nn.AdaptiveMaxPool2d(output_size=output_size)

    def init_adaptive_avgpool_2d(self, output_size):
        return nn.AdaptiveAvgPool2d(output_size=output_size)

    def build_from_model(self, model_name, output_dim):

        self.model = self.named_models[model_name]

        if "mobilenet" in model_name:
            self.model.classifier = nn.Linear(
                in_features = 1280, 
                out_features = output_dim
            )
        
        if "resnet" in model_name:
            self.model.fc = nn.Linear(
                in_features = self.model.fc.in_features,
                out_features = output_dim
            )


t = Trainer()

a = [   ("linear", [10,10]), ("conv_2d", [100,200, (1,1), (2,2)] ), ("dropout", [1])   ]
t.build_from_skratch(a)

print(t.model)


