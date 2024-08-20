from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
import json
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from PIL import Image
from .models import MyModel
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
from cloudinary.uploader import upload




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
        #   # Save the image to the model, which uploads it to Cloudinary
        # my_model_instance = MyModel(image=fileObj)
        # my_model_instance.save()

        img = Image.open(fileObj)
    
        # Resize the image
        img = img.resize((224, 224))  # Resize to 224x224 pixels (or any size you prefer)
    
        # Convert the image to a format suitable for your model
        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        img_io.seek(0)
    
    # Load the image using load_img from keras or any other function for processing
    # Make sure the function accepts BytesIO objects or convert it to the required format

        # Load the image from the URL
        img = load_img(img_io, target_size=(img_height, img_width))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # Make prediction
        predictions = model.predict(x)
        predictions = decode_predictions(predictions, top=1)[0]
        class_labels = predictions[0][1]

        

        # Get the URL of the uploaded image
        #filePathName = my_model_instance.image.url
         filePathName = img_io


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
