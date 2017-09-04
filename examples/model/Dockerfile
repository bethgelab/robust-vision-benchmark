FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

# set workdir to the home directory
WORKDIR /root

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# install python and other tools
RUN apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get install -yq -qq --no-install-recommends \
    build-essential \
    curl \
    git \
    libssl-dev \
    python3 \
    python3-pip \
    unzip \
    wget \
    zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install required python packages
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir setuptools
RUN pip3 install --no-cache-dir foolbox
RUN pip3 install --no-cache-dir robust_vision_benchmark

# install your requirements
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# add your model script
COPY main.py main.py

# add your weights (to avoid redownloading them for every container start)
COPY data/ /root/.keras/

CMD ["python3", "./main.py"]
