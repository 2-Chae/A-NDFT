## Installation

We strongly recommend that users reproducing experimental results use the following docker image:
- [pytorch/pytorch:0.4.1-cuda9-cudnn7-devel](https://hub.docker.com/layers/pytorch/pytorch/0.4.1-cuda9-cudnn7-devel/images/sha256-3febd5b72fb0b90d646060b64cf2063ea9fe2a2f4b17e06cba675a611adfbaea?context=explore)
- For version consistency,
  - `pip install torch==1.0.1 torchvision==0.2.0 -f https://download.pytorch.org/whl/torch_stable.html`.
  - `python==3.6.13`, `numpy==1.19.5`, `Pillow==8.2.0`, and `scipy==1.2.0`

1. Run:
```shell
cd ./lib
python setup.py build develop
sh ./make.sh
```
if you encounter `error: invalid command 'develop'`, follow this one 
[https://github.com/django-extensions/django-extensions/issues/92](https://github.com/django-extensions/django-extensions/issues/92)


2. Download the file([nms_cuda.c](https://c11.kr/ls8k)). Unzip & place it in the path ./lib/model/nms/src


3. Run:
```shell
cd ./lib/model/nms
sh make.sh
```

