from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications.mobilenet import preprocess_input,decode_predictions
import json
import numpy as np

import tensorflow as tf

img_height, img_width=224,224
with open('./models/imagenet_classes.json', 'r') as f:
     labelInfo=f.read()
labelInfo=json.loads(labelInfo)
model=load_model('./models/mobilenet_imagenet.h5')



# model_graph = tf.Graph()
# Create a session within that graph
# with model_graph.as_default():
#     tf_session=tf.compat.v1.Session()
#     with tf_session.as_default():
#         model=load_model('./models/MobileModelImagenet_model.h5')

# Create your views here.
def index_img(request):
    return render(request,'index_img.html')

def predict_img(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)


    test_image='.'+filePathName
    img=load_img(test_image, target_size=(img_height, img_width))
    x=img_to_array(img)
    x=np.expand_dims(x, axis=0)
    x=preprocess_input(x)

    predictions=model.predict(x)
    predictions=decode_predictions(predictions, top=1)[0]
    class_labels= [prediction[1] for prediction in predictions][0]

    # x=x/255
    # x=x.reshape(1,img_height,img_width,3)
    # with model_graph.as_default():
    #     tf_session=tf.compat.v1.Session()
    #     with tf_session.as_default():
    #         pred=model.predict(x)
    
    # predictedLabel=labelInfo[str(np.argmax(pred[0]))]

    context={'filePathName':filePathName,'predictedLabel':class_labels}
    return render(request,'result.html',context)