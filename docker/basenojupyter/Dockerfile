ARG BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

# Install common tools, Tensorflow, OpenCV, GStreamer, and miscellaneous dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        net-tools vim cmake gfortran build-essential liblapack-dev libblas-dev \
        libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev \
        libopencv-python libwayland-egl1 gstreamer1.0-plugins-bad \
        libgstreamer-plugins-bad1.0-0 gstreamer1.0-plugins-good python3-gst-1.0 \
        supervisor unzip python3-smbus && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install setuptools Cython wheel h5py==2.10.0 --verbose && \
    pip3 install future==0.17.1 mock==3.0.5 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11 numpy --verbose

# Install Tensorflow
ARG TENSORFLOW_URL=https://nvidia.box.com/shared/static/rummpy6q1km1wivomalpkwt2jy28mndf.whl 
ARG TENSORFLOW_WHL=tensorflow-1.15.2+nv-cp36-cp36m-linux_aarch64.whl
RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${TENSORFLOW_URL} -O ${TENSORFLOW_WHL} && \
    pip3 install ${TENSORFLOW_WHL} --verbose && \
    rm ${TENSORFLOW_WHL}

# Install torch2trt
ENV TORCH2TRT_REPO_DIR=/opt/
RUN cd ${TORCH2TRT_REPO_DIR} && \
    git clone https://github.com/NVIDIA-AI-IOT/torch2trt && \
    cd torch2trt && \
    python3 setup.py install
