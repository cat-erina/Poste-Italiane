
import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu
import cv2
import os
import numpy as np
import pandas as pd

model_path = os.path.join('/Users/caterina/Documents/DataScience/PosteItaliane/model','Secondo.h5')
model = models.load_model(model_path, backbone_name='resnet50')
labels_to_names = {0: 'dummy', 1: 'large block buildings', 2: 'small villas'}
path=os.listdir('/Users/caterina/Documents/DataScience/PosteItaliane/TrainingCamp_Data/Test_set/images/')
l=[]

for img in path:
    if (".jpg") in img:
        image = read_image_bgr('/Users/caterina/Documents/DataScience/PosteItaliane/TrainingCamp_Data/Test_set/images/'+img)
        image = preprocess_image(image)
        image, scale = resize_image(image)
        boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
        boxes /= scale
        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score < 0.4:
                break
            l.append([img,str(box[0]).replace(".",","),str(box[1]).replace(".",","),str(box[2]).replace(".",","),str(box[3]).replace(".",","),label,str(score).replace(".",",")])

Out=pd.DataFrame(l, columns=["Image","xMin","yMin","xMax","yMax","Class","Confidence"])
Out.to_csv("Output_2.csv", sep=";")

