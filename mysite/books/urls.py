
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #/books/2/
    path('<str:book_id>/', views.detail, name='detail'),
]
