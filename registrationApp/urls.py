from django.urls import path
from registrationApp import views



urlpatterns = [
    path('login/', views.login_fun, name='login_page'),
    path('sign_up/', views.sign_upfun, name='sign_up'),
    path('logout/',views.LogoutPage, name='logout')
]