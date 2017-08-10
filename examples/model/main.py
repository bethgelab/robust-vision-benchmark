#!/usr/bin/env python3

import keras
from keras.applications.resnet50 import ResNet50

from foolbox.models import KerasModel
from robust_vision_benchmark import imagenet_model_server

keras.backend.set_learning_phase(0)
kmodel = ResNet50(weights='imagenet')
preprocessing = ([104, 116, 123], 1)
fmodel = KerasModel(kmodel, bounds=(0, 255), preprocessing=preprocessing)

imagenet_model_server(fmodel, channel_order='BGR', image_size=224)
