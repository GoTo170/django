from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('index', views.index2, name='index2'),
]
