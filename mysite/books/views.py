from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book

def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        path = '/books/' + str(book.id) + '/'
        html += '<a href = "' + path + '">' + str(book.name) + '</a><br>'

    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2>Details for Book ID:" + str(book_id) + "</h2>")