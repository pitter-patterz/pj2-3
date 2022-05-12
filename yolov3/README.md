# Introduction
This is the second task of project 2. Here uses yolov3 to do classfication on VOC-2007 datasets. The Implementation of this model is referred to https://github.com/ultralytics/yolov3
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
