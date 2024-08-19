from django.shortcuts import render,HttpResponse
import joblib

model=joblib.load('static/random_forest_regressor_trained')

# Create your views here.
def index(request):
    #return HttpResponse(" This is the Home Page!!!!!!!")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def prediction(request):
    if request.method=='POST':
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        bmi=request.POST.get('bmi')
        children=request.POST.get('children')
        smoker=request.POST.get('smoker')
        region=request.POST.get('region')

        print(age,bmi,sex,children,smoker, region)
        pred=round(model.predict([[age, sex, bmi, children, smoker, region ]])[0])
        #print(pred)
        output={"output":pred}

        return render(request, 'prediction.html',output )
    else:
        return render(request, 'prediction.html')