from django.urls import path
from img_cls_App import views

urlpatterns = [
    path('', views.index_img, name='img_classification'),
    path('predict_img/', views.predict_img, name='predict_img')
]