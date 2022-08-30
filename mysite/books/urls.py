
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    #/books/2/
    path('<str:book_id>/', views.detail, name='detail'),
]
