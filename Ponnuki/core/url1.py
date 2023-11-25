# core/urls.py
from django.urls import include, path
from . import views
from .views import *

app_name = 'core'




urlpatterns = [
   
    path('',views.main ,name='main'),
    path('main/',views.main ,name='main'),
    path('shop/', views.shop, name='shop'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact , name='contact'),
    path('login/', views.login, name='login'),
    path('sign_up/',views.sign_up,name='sign_up'),
    #path('asd/',views.my_view),
    #path('main/', GenericPageView.as_view(template_name='core/main.html'), name='main'),
    #path('index/',views.index,name='index'),
    # Add more paths for each page
]
