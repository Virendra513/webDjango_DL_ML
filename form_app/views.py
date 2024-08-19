from django.shortcuts import render
from form_app.models import ContactEnquiry

# Create your views here.
def form_func(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data=ContactEnquiry(name=name,email=email,message=message)
        data.save()
    return render(request,'contact.html')

    
