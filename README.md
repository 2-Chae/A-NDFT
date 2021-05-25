# A-NDFT

PyTorch Code for the paper:  
**"Training Domain-invariant Object Detector Faster with Feature Replay and Slow Learner"**  
Chaehyeon Lee, Junghoon Seo and Heechul Jung.

Original code is [UAV-NDFT](https://github.com/VITA-Group/UAV-NDFT) from VITA-Group.  
Based on the original code, we implemented feature replay and slow learner additionally.

```BibTex
@InProceedings{Lee_2021_CVPR_Workshops,
author = {Lee, Chaehyeon and Seo, Junghoon and Jung, Heechul},
title = {Training Domain-invariant Object Detector Faster with Feature Replay and Slow Learner},
booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month = {June},
year = {2021}
}
```

## Installation
### Prerequisites
- Linux or macOS (Windows is in experimental support)
- Python 3.6 +
- PyTorch 0.4.1
- TorchVision 0.2.1
- CUDA 9.1

See [get_started.md](docs/get_started.md).


## Multiple GPU Training
```{r, engine='bash', count_lines}
#!/bin/bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python trainval_net_monitor.py --cuda --mGPUs --gamma_weather 0.01  --gamma_angle 0.01 --gamma_altitude 0.01 --use_adversarial_loss --bs 32 --ema-beta 0.99 
```

## Single GPU Training
```{r, engine='bash', count_lines}
#!/bin/bash
for ((i=0; i<=10; i++))
do
        epoch=$(($i*1000/11914+1))
        ckpt=$((i*1000%11914))
        echo "$epoch"
        echo "$ckpt"
        CUDA_VISIBLE_DEVICES=0 python test_net.py --cuda --checkepoch "$epoch" --checkpoint "$ckpt" --gamma 0.5
done

```
## UAVDT Data (Training+Testing) in Pascal Voc Format
Google Drive: https://drive.google.com/file/d/13xdLBfIWGYrjpT0Z3miAPKnKNDjNqLS9/view?usp=sharing

## UAVDT Trained Model (w/o Adversarial Loss and w/ Adversarial Loss)
Google Drive: https://drive.google.com/file/d/1rxqr0Cq0y9cXhdWyNd_R_8cd68exD1wn/view?usp=sharing

We use models/baseline/faster_rcnn_1_4_3960.pth as pretrained model.


## Project Directory Layout
```
.
├── cfgs
├── data              # UAVDT dataset with annotation
├── images
├── lib
├── logs              # TensorBoard event files
├── models            # Trained model (w/ adversarial loss and w/o adversarial loss)
├── output
├── summaries         # Summary files recording the training and validation performance
├── README.md
├── _init_paths.py
├── bash_run.sh       # Run the testing in batch
├── demo.py
├── requirements.txt
├── test_net.py
├── trainval_net.py
└── trainval_net_monitor.py
```
