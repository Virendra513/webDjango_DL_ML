from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import MyModel
from cloudinary.uploader import upload
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

# Create your views here.
def index_img(request):
    return render(request,'index_img.html')

def predict_img(request):
     if request.method == 'POST' and 'filePath' in request.FILES:
        fileObj = request.FILES['filePath']

        # Save the image to the model, which uploads it to Cloudinary
        my_model_instance = MyModel(image=fileObj)
        my_model_instance.save()

        # Get the URL of the uploaded image
        filePathName = my_model_instance.image.url

        # Load the image from the URL
        img = load_img(filePathName, target_size=(img_height, img_width))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # Make prediction
        predictions = model.predict(x)
        predictions = decode_predictions(predictions, top=1)[0]
        class_labels = predictions[0][1]

        # Prepare context for rendering the result
        context = {'filePathName': filePathName, 'predictedLabel': class_labels}
        return render(request, 'result.html', context)
     return render(request, 'index_img.html')
     



     
    # fileObj=request.FILES['filePath']
    # fs=FileSystemStorage()
    # filePathName=fs.save(fileObj.name,fileObj)
    # filePathName=fs.url(filePathName)


    # test_image='.'+filePathName
    # img=load_img(test_image, target_size=(img_height, img_width))
    # x=img_to_array(img)
    # x=np.expand_dims(x, axis=0)
    # x=preprocess_input(x)

    # predictions=model.predict(x)
    # predictions=decode_predictions(predictions, top=1)[0]
    # class_labels= [prediction[1] for prediction in predictions][0]



    # context={'filePathName':filePathName,'predictedLabel':class_labels}
    # return render(request,'result.html',context)
