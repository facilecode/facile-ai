import torch
import torchvision
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as trans
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.nn.functional as F
from PIL import Image
import cv2
from time import sleep
import os

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
    train_transforms_augm = trans.Compose([
        trans.RandomResizedCrop(224),
        trans.RandomHorizontalFlip(),
        trans.ColorJitter(brightness=(0.10,0.9), contrast=(0.10,0.9)),
        trans.ToTensor(),
        trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    train_transforms = trans.Compose([
        trans.Resize(224),
        trans.ToTensor(),
        trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    test_transforms = trans.Compose([
        trans.Resize((224,224)),
        trans.ToTensor(),
        trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


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
        self.train_transforms = None
        self.test_transforms = None
        self.classes = None
        self.classes_num = None
        self.init_train_transforms(True)
        self.init_test_transforms()
        
    

    # network components
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

    # building model
    def build_from_model(self, model_name, pretrained, output_dim):

        if "mobilenet" in model_name and "v2" in model_name:
            self.model = models.mobilenet_v2(pretrained=pretrained)
            self.model.classifier = nn.Sequential(
                nn.Linear(
                    in_features = 1280, 
                    out_features = output_dim
                ), 
                nn.Sigmoid()
            )
        
        if "resnet" in model_name:
            if "18" in model_name:
                self.model = models.resnet18(pretrained=pretrained)
            if "34" in model_name:
                self.model = models.resnet34(pretrained=pretrained)
            if "50" in model_name:
                self.model = models.resnet50(pretrained=pretrained)
            if "101" in model_name:
                self.model = models.resnet101(pretrained=pretrained)
            if "152" in model_name:
                self.model = models.resnet152(pretrained=pretrained)  

            self.model.fc = nn.Sequential(
                nn.Linear(
                    in_features = self.model.fc.in_features,
                    out_features = output_dim
                ),
                nn.Sigmoid()
            )

        if "squeezenet" in model_name:
            if "1.0" in model_name:
                self.model = models.squeezenet1_0(pretrained=pretrained)
            if "1.1" in model_name:
                self.model = models.squeezenet1_1(pretrained=pretrained)

            self.model.classifier[1] = nn.Conv2d(512, output_dim, kernel_size=(1,1), stride=(1,1))
        
        if "densenet" in model_name:
            if "121" in model_name:
                self.model = models.densenet121(pretrained=pretrained)
            if "161" in model_name:
                self.model = models.densenet161(pretrained=pretrained)
            if "169" in model_name:
                self.model = models.densenet169(pretrained=pretrained)
            if "201" in model_name:
                self.model = models.densenet201(pretrained=pretrained)
            
            self.model.classifier = nn.Linear(
                in_features = self.model.classifier.in_features, 
                out_features = output_dim)

        if "inception" in model_name and "v3" in model_name:
            self.model = models.inception_v3(pretrained=pretrained)
            self.model.AuxLogits.fc = nn.Linear(
                in_features=768,
                out_features=output_dim
            )
            self.model.fc = nn.Linear(
                in_features = self.model.fc.in_features, 
                out_features = output_dim)
        
        if "vgg" in model_name:
            if "bn" in model_name:
                if "11" in model_name:
                    self.model = models.vgg11_bn(pretrained=pretrained)
                if "13" in model_name:
                    self.model = models.vgg13_bn(pretrained=pretrained)
                if "16" in model_name:
                    self.model = models.vgg16_bn(pretrained=pretrained)
                if "19" in model_name:
                    self.model = models.vgg19_bn(pretrained=pretrained)
            else:
                if "11" in model_name:
                    self.model = models.vgg11(pretrained=pretrained)
                if "13" in model_name:
                    self.model = models.vgg13(pretrained=pretrained)
                if "16" in model_name:
                    self.model = models.vgg16(pretrained=pretrained)
                if "19" in model_name:
                    self.model = models.vgg19(pretrained=pretrained)
            
            self.model.classifier[6] = nn.Linear(self.model.classifier[6].in_features, output_dim)
        
        if "alexnet" in model_name:
            self.model = models.alexnet(pretrained=pretrained)
            self.model.classifier[6] = nn.Linear(self.model.classifier[6].in_features, output_dim)

        self.model.eval()
    
    def build_from_skratch(self, arch):

        layers = []
        for name, args in arch:
            
            layer = self.named_layers[name](name)

            layers.append(layer)
            layer = None
        
        self.model = nn.Sequential(nn.ModuleList(layers))

    # transform methods
    def init_train_transforms(self, data_augm):
        
        if data_augm == True:
            self.train_transforms = trans.Compose([
                trans.RandomResizedCrop(224),
                trans.RandomHorizontalFlip(),
                trans.ColorJitter(brightness=(0.10,0.9), contrast=(0.10,0.9)),
                trans.ToTensor(),
                trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ])
        else:
            self.train_transforms = trans.Compose([
                trans.Resize(224),
                trans.ToTensor(),
                trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ])

    def init_test_transforms(self):
        
        self.test_transforms = trans.Compose([
            trans.Resize((224,224)),
            trans.ToTensor(),
            trans.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    # optimizers
    def init_optim(self, optim_name, parameters, lr, fine_tune):
        pass
    # dataset
    def load_dataset(self, dataset_path):
        pass
    # train
    def train(self, dataset_path, data_augm, epoch, fine_tune, optimizer_name, loss_name, lr, gpu):

        self.classes = os.listdir(dataset_path)
        self.classes_num = len(self.classes)

        if data_augm == True:
            transform = self.train_transforms_augm
        else:
            transform = self.train_transforms
        
        # to-do : separate dataset into train/val

        trainset = torchvision.datasets.ImageFolder(
            root=dataset_path + '/train', transform=transform)
        trainloader = torch.utils.data.DataLoader(trainset, batch_size=8,
                                                shuffle=True, num_workers=8)
        testset = torchvision.datasets.ImageFolder(
            root=dataset_path + '/val', transform=transform)
        testloader = torch.utils.data.DataLoader(testset, batch_size=8,
                                                shuffle=False, num_workers=8)
        dataloaders_dict = {
            'train': trainloader,
            'val': testloader
        }

        self.build_from_model("mobilenet v2", pretrained=True, output_dim=self.classes_num)

        #to-do : optimizers ...
        optimizer = self.init_optim()

    # predict on image from image_path
    def predict(self, image_path):
        im = cv2.imread(image_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(im)

        im = self.test_transforms(im).unsqueeze(0)

        output = self.model(im)
        _, preds = torch.max(output, 1)

        print(preds)


t = Trainer()   
t.train("dataset", data_augm=True, epoch=5, fine_tune=True, optimizer_name="SGD", loss_name="x_entropy", lr = 0.001, gpu=False)