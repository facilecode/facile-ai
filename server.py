 
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from requests import post, get
from time import sleep, time
import random
import os
from threading import Thread
import sys
import signal
from threading import Thread
# ml
import sklearn
# dl
import torch
import torch.nn as nn
import torchvision
print("PyTorch imported")
import tensorflow as tf 
print("Tensorflow imported")

DEBUG = True

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

def build_pytorch_model(architecture):

    named_layer = {
        "activation": nn.ReLU(),
        "layer": nn.Linear(1,1),
        "conv": nn.Conv2d(1,1,1),
    }

    print(architecture, type(architecture))

    layers = [named_layer[layer] for layer in architecture ]

    try:
        model = nn.Sequential(nn.ModuleList(layers))
    except Exception as e:
        print("couldnt create model", e)
    
    print(model)

@app.route('/')
def hello_world():
    return "hello_world"

global step
step = 0

@app.route('/train', methods=['POST', 'GET'])
def train():
    global step

    if request.method == "GET":
        return str(step)
    
    if request.method == "POST":
        data = json.loads(request.get_data())
        print(type(data), data)
        return "ok"

@app.route('/arch', methods=['POST', 'GET'])
def receive():
    arch = json.loads(request.get_data())
    
    build_pytorch_model(arch["arch"])
    
    return "ok from /arch"

app.run(host="127.0.0.1", port=3000)