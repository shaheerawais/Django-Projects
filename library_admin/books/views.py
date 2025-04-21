from django.shortcuts import render, get_object_or_404
from .models import Book, Review

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})
