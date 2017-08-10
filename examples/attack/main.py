#!/usr/bin/env python3

from foolbox.attacks import FGSM
from robust_vision_benchmark import attack_server

fgsm = FGSM()

attack_server(fgsm)
