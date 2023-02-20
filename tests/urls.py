from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scanning_page/', views.scanning_page, name='scanning_page'),
]
