from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('contact/', views.contact, name='contact'),
    path('sp/', views.satellite_position, name='satellite_position'),
    path('ul/', views.upcoming_launches, name='upcoming_launches'),
    path('aopd/', views.astronomical_picture, name='astronomical_picture'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
]


