from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),          
    path('about/', views.about, name='about'),       
    path('project/', views.project, name='project'), 
    path('resume/', views.resume_list, name='resume_list'),  
    path('contact/', views.contact_view, name='contact'),     
]
