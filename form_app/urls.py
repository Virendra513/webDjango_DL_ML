from django.urls import path
from form_app import views

urlpatterns = [
    path('', views.form_func, name='form_data')
]