from django.contrib import admin
from django.urls import path
from portfolio import views
from portfolio.views import contact_view

urlpatterns = [
    path('', views.index, name='index'),  # Home Page
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('resume/', views.resume_list, name='resume_list'),  # Dynamic resume page
    path('contact/', contact_view, name='contact'),  # Contact form saving to DB
]