from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('index/', views.index, name='index'),
]