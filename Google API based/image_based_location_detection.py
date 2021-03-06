# -*- coding: utf-8 -*-
"""Image based location detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/aayushkumar20/ML-based-projects./blob/main/Google%20API%20based/Image_based_location_detection.ipynb
"""

#Install this first for complete functioning
!pip install -q gradio
#!pip install "tf-nightly" 
#There might be some issue with the older version of Tensorflow 
#If the interpreter shows some error then please try to install (!pip install "tf-nightly") and re interprete it.
#Like "module 'tensorflow_hub' has no attribute 'KerasLayer'"

# Modules required for the complition
# Importing the modules

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import gradio as gr
import PIL.Image as Image
import tensorflow as tf
import tensorflow_hub as hub

"""**Make sure to install all the modules and 'gradio modules' before interpreting.**"""

TF_MODEL_URL = 'https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_asia_V1/1'
LABEL_MAP_URL = 'https://www.gstatic.com/aihub/tfhub/labelmaps/landmarks_classifier_asia_V1_label_map.csv'
IMAGE_SHAPE = (321, 321)

classifier = tf.keras.Sequential([hub.KerasLayer(TF_MODEL_URL,
                                                 input_shape=IMAGE_SHAPE+(3,),
                                                 output_key="predictions:logits")])

df = pd.read_csv(LABEL_MAP_URL)

label_map = dict(zip(df.id, df.name))

img_loc = "Image.jpeg" #Please change this to the location of your image including directory.
#In case you are using it on your windows machine please mention the entire path.
#Please make sure you have the same name of image as above i.e.(Image.jpeg) you can rename it as your choice.
#In case you are using it on "google colab" then please make sure that you have mounted the image file and also the mounting location with file name.

img=Image.open(img_loc).resize(IMAGE_SHAPE)

"""**in order to check whether your image is sucessfully added you can type (img)**"""

img
#to check
#if not detected the please try to follow the instruction in the above 2 lines.

img = np.array(img)/255.0
img.shape

img = img[np.newaxis, ...]

img.shape

result = classifier.predict(img)

result
#it'll contain the probablity values and length of the model.

label_map[np.argmax(result)]
#it'll predict the location by using the "classifier.predict"

class_names=list(label_map.values())

def classify_image(image):
    img = np.array(image)/255.0
    img = img[np.newaxis, ...]
    prediction = classifier.predict(img)
    return label_map[np.argmax(prediction)]

"""**UI for user interaction**"""

image = gr.inputs.Image(shape=(321, 321))
label = gr.outputs.Label(num_top_classes=1)

gr.Interface(
    classify_image,
    image,
    label,
    capture_session=True,).launch(debug=True);