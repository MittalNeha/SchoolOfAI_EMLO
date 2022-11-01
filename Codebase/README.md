<div align="center">

# Lightning-Hydra-Template

[![python](https://img.shields.io/badge/-Python_3.7_%7C_3.8_%7C_3.9_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_1.8+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_1.6+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.2-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![pre-commit](https://img.shields.io/badge/Pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![tests](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/ashleve/lightning-hydra-template/branch/main/graph/badge.svg)](https://codecov.io/gh/ashleve/lightning-hydra-template)
[![code-quality](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/ashleve/lightning-hydra-template#license)
[![contributors](https://img.shields.io/github/contributors/ashleve/lightning-hydra-template.svg)](https://github.com/ashleve/lightning-hydra-template/graphs/contributors)

<!-- <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-Python 3.7+-blue?style=for-the-badge&logo=python&logoColor=white"></a> -->

<!-- <a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning 1.6+-792ee5?style=for-the-badge&logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: hydra" src="https://img.shields.io/badge/config-hydra 1.2-89b8cd?style=for-the-badge&labelColor=gray"></a>
<a href="https://black.readthedocs.io/en/stable/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg?style=for-the-badge&labelColor=gray"></a> -->

A clean and scalable template to kickstart your deep learning project 🚀⚡🔥<br>
Click on [<kbd>Use this template</kbd>](https://github.com/ashleve/lightning-hydra-template/generate) to initialize new repository.

_Suggestions are always welcome!_

</div>

<br>

## Session 4. Deployment of Demos
1. Basic Demo Using Gradio<br>
    Files Committed: configs/demo.yaml, src/demo.py

    #### Train first to generate the checkpoint
    ```
    python3 src/train.py experiment=example
    ```
    #### Then run the demo
    ```
    python src/demo.py ckpt_path=/home/ubuntu/lightning-hydra-template/logs/train/runs/2022-09-01_02-38-23/checkpoints/last.ckpt experiment=example
    ```
2. Scripted Demo with TorchScript<br>
    Files Commited: configs/demo_scripted.yaml, src/demo_scripted.yaml.py

3. Running CIFAR10 Demo from Docker image
    - Download the Docker image from [https://hub.docker.com/repository/docker/mittalneha28/session4_demo]()
    - To run the docker use the command
    ```
    docker run -t -p 8080:8080 mittalneha28/session4_demo
    ```

## Session 3. Changes implemented for Step-wise logging, Optuna Hyperparam tuning and DVC push

**Code Changes**

- The cifar10_optuna.yaml file is configured with optuna sweeper configurations (Hyperparam sweep), tensorboard logging alongside the datamodule and model (resnet18) specifications.
- In timm_module.py file, step-wise logging has been enabled for training and validation using the option "on_step=True"
- The validation loss is logged as "hp_metric" in tensorboard.
- The training is run for 8 trial with 2 epochs in each trial.
- The best batch_size, learning rate, and optimizer are obtained at the end of training.

- Command used for training the model (Trained in Google colab using GPU)

```
!python src/train.py -m hparams_search=cifar10_optuna 
```

- The data and logs folders are pushed to Google Drive using DVC.

```
!dvc init -f

!git rm -r --cached 'data'
!dvc add data

!git rm -r --cached 'logs'
!dvc add logs

!git add .
!dvc config core.autostage true

!dvc remote add gdrive -f gdrive://<drive id>

!dvc push -r gdrive
```

## Changes implemented on the template and the MAKE commands

**Code Changes**

- Timm pretrained model has been integrated, with timm.create_model as target and resnet18 as the model_name
- CIFAR10 DataModule has been added (cifar10_datamodule.py in src/datamodules, cifar10.yamlin configs/datamodule)
- The model is trained using the experiment yaml file, cifar10.yaml in configs/experiment.

**Makefile**

- The below commands have been added in the Makefile to build the Docker image, mount the the volume to Docker Container and run the train.py.

_build:_

```
docker build -t ${IMAGE_NAME} .
```

_run:_

```
docker run -it --volume `pwd`:/workspace/project emlov2-session-02:latest python3 src/train.py experiment=cifar10.yaml
```
