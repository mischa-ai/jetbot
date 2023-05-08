# Base Image

This is the optimized base image that includes

* PyTorch
* TensorFlow
* Torch2Trt
* JetBot Python API

Among other small related dependencies.

```bash
cd docker/base
./build.sh
```

Other images depend on this, it's typically not run directly.  You can 
build your own image on top of this.
