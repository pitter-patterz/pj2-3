# Introduction
This is the third task of project 2. We use yolov3 to do object detection on VOC2007 images. The Implementation of this model is referred to https://github.com/ultralytics/yolov3.

# Usage
Train data on VOC dataset. If you want to change the hyperparameters, please modified the data/hyps/hyp.scratch.yaml.
```python
python train.py
```
For testing data on VOC dataset, runs
```python
python test.py
```
For detecting data on custom dataset, runs
```python
python detect.py --source dataset_path
```
You should first download the model weights file and put it under this folder before runs detect.py. The model parameters can be downloaded from
link：https://pan.baidu.com/s/1anyqWPLHFTJfw_bmdXvG1w 
pwd：nd9t
