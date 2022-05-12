# Introduction
This is the third task of project 2. We use yolov3 to do object detection on VOC2007 images. 

The Implementation of this model is referred to https://github.com/ultralytics/yolov3.

# Usage
Train data on VOC dataset. If you want to change the hyperparameters, please modified the data/hyps/hyp.scratch.yaml.
```python
python train.py
```
For testing on VOC dataset
```python
python test.py
```
For detecting on custom dataset
```python
python detect.py --source dataset_path
```
You should first download the model weights file and put it under this folder before running detect.py. 

Link: https://pan.baidu.com/s/1anyqWPLHFTJfw_bmdXvG1w (pwd：nd9t)
