.. image:: https://travis-ci.org/bethgelab/robust-vision-benchmark.svg?branch=master
    :target: https://travis-ci.org/bethgelab/robust-vision-benchmark

=======================
Robust Vision Benchmark
=======================

This Python package provides utility functions to create submissions for the `Robust Vision Benchmark <https://robust.vision/benchmark>`__ and scripts to automatically test and upload them. You might also want to have a look at `Foolbox <https://github.com/bethgelab/foolbox>`__, our python toolbox to benchmark the robustness of machine learning models using a large set of adversarial attacks.

Installation
------------

We test using Python 2.7, 3.5 and 3.6. Other Python versions might work as well, but we recommend using Python 3.5 or newer.

.. code-block:: bash

   pip install robust-vision-benchmark

Submitting a model
------------------

A model submission consists of a Dockerfile, a script (e.g. Python) and data (e.g. network weights).

Python script
^^^^^^^^^^^^^

Create a Python script that turns your model into a Foolbox model using one of our wrappers for TensorFlow, PyTorch, Theano, Keras, Lasagne, MXNet and starts the `model_server`.

.. code-block:: python

   from robust_vision_benchmark import model_server

   # create your model
   # ...

   # turn it into a Foolbox model
   model = foolbox.models.SomeModel(...)

   # start the server
   mnist_model_server(model)
   cifar_model_server(model, channel_order='RGB or BGR')
   imagenet_model_server(model, channel_order='RGB or BGR', image_size=224)

   # For CIFAR and Imagenet, the channel_order must be set to either 'RGB' or 'BGR'.
   # For ImageNet, the image_size must be set to an integer (usually 224 vor VGG-like networks and 299 for inception-like networks).

Dockerfile
^^^^^^^^^^

Create a Dockerfile that installs all dependencies and starts the script.

.. code-block:: Dockerfile

   FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

   RUN apt-get update ... && install ...

   RUN pip3 install --no-cache-dir robust-vision-benchmark

   ...

   COPY main.py main.py

   CMD ["python3", "./main.py"]

For compatibility with our backend, please use a derivative of the `nvidia/cuda:8.0` image (e.g. `nvidia/cuda8.0-cudnn5-devel-ubuntu16.04`) as the base image or contact us if you have special requirements.

Test the submission
^^^^^^^^^^^^^^^^^^^

Put the Dockerfile, script, data and other required files into a folder, e.g. *model* and run the following in your shell:

.. code-block:: bash

   rvb-test-model model/

You can find an example in *examples/model/*.

Upload the submission
^^^^^^^^^^^^^^^^^^^^^

Once your model is ready for submission, upload it:

.. code-block:: bash

   rvb-upload model/

Submitting
^^^^^^^^^^

Go to https://robust.vision/benchmark/participate and put the URL returned by the upload script into the `Submission URL`.

Submitting an attack
--------------------

An attack submission consists of a Dockerfile and a script (e.g. Python).

Python script
^^^^^^^^^^^^^

Create a Python script that implements your attack and starts the `attack_server`.

.. code-block:: python

   from robust_vision_benchmark import attack_server

   # implement your attack
   def attack(a):
       # ...

   # start the server
   attack_server(attack)

Dockerfile
^^^^^^^^^^

Create a Dockerfile that installs all dependencies and starts the script.

.. code-block:: Dockerfile

   FROM python:3.6

   RUN pip3 install --no-cache-dir robust-vision-benchmark

   ...

   COPY main.py main.py

   CMD ["python3", "./main.py"]

Test the submission
^^^^^^^^^^^^^^^^^^^

Put the Dockerfile, script and other required files into a folder, e.g. *attack* and run the following in your shell:

.. code-block:: bash

   rvb-test-attack attack/

You can find an example in *examples/attack/*.

Upload the submission
^^^^^^^^^^^^^^^^^^^^^

Once your attack is ready for submission, upload it:

.. code-block:: bash

   rvb-upload attack/

Submitting
^^^^^^^^^^

Go to https://robust.vision/benchmark/participate and put the URL returned by the upload script into the `Submission URL`.

Authors
-------

* `Jonas Rauber <https://github.com/jonasrauber>`_
* `Wieland Brendel <https://github.com/wielandbrendel>`_

