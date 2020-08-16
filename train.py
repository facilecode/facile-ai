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

DEBUG = True

app = Flask(__name__)

def train(n):
    for i in range(n):
        sleep(1)
        #post("http://127.0.0.1:3000/train", data=i)

Thread(target=train, args=(100,)).start()
