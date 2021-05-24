## Installation

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

