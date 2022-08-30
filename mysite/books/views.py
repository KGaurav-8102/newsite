from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book
from django.shortcuts import render

def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books' : all_books
    }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    return HttpResponse("<h2>Details for Book ID:" + str(book_id) + "</h2>")