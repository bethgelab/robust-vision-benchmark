FROM python:3.6

# set workdir to the home directory
WORKDIR /root

# install required packages
RUN pip3 install --no-cache-dir foolbox
RUN pip3 install --no-cache-dir robust_vision_benchmark

# install other python packages
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# add your model script
COPY main.py main.py

CMD ["python3", "./main.py"]
