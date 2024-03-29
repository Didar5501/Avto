from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/', views.brand, name='brand'),
    path('model/', views.model, name='model'),
    path('color/', views.color, name='color'),
]