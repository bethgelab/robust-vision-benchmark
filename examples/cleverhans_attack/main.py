#!/usr/bin/env python3

import tensorflow as tf
import numpy as np
from cleverhans.attacks import FastGradientMethod
from robust_vision_benchmark import attack_server
from utils import FoolboxToCleverhansModel


def attack(a):
    session = tf.Session()
    with session.as_default():
        model = FoolboxToCleverhansModel(a)
        fgsm = FastGradientMethod(model, sess=session)
        adversarial_image = fgsm.generate_np(a.original_image[np.newaxis])
        adversarial_image = np.squeeze(adversarial_image, axis=0)
        # optionally, reset to ignore other adversarials
        # found during the search
        a._reset()
        # run predictions to make sure the returned adversarial
        # is taken into account
        min_, max_ = a.bounds()
        adversarial_image = np.clip(adversarial_image, min_, max_)
        a.predictions(adversarial_image)


attack_server(attack)
