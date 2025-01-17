from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Borrower, Category

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def add_book(request):
    borrowers = Borrower.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        borrower_id = request.POST.get('borrower')
        category_id = request.POST.get('category')

        borrower = Borrower.objects.get(id=borrower_id) if borrower_id else None
        category = Category.objects.get(id=category_id) if category_id else None

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year,
            borrower=borrower,
            category=category
        )
        return redirect('index')

    return render(request, 'books/add-book.html', {'borrowers': borrowers, 'categories': categories})

def borrowed_books(request):
    books = Book.objects.filter(is_borrowed=True)
    return render(request, 'books/borrowed-books.html', {'books': books})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('index')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowers = Borrower.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')

        borrower_id = request.POST.get('borrower')
        book.borrower = Borrower.objects.get(id=borrower_id) if borrower_id else None

        category_id = request.POST.get('category')
        book.category = Category.objects.get(id=category_id) if category_id else None

        book.save()
        return redirect('index')

    return render(request, 'books/edit-book.html', {'book': book, 'borrowers': borrowers, 'categories': categories})

def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'books/borrower_list.html', {'borrowers': borrowers})

def add_borrower(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Borrower.objects.create(name=name, email=email)
        return redirect('borrower_list')
    return render(request, 'books/add_borrower.html')

def edit_borrower(request, borrower_id):
    borrower = get_object_or_404(Borrower, id=borrower_id)
    if request.method == 'POST':
        borrower.name = request.POST.get('name')
        borrower.email = request.POST.get('email')
        borrower.save()
        return redirect('borrower_list')
    return render(request, 'books/edit_borrower.html', {'borrower': borrower})

def delete_borrower(request, borrower_id):
    borrower = get_object_or_404(Borrower, id=borrower_id)
    borrower.delete()
    return redirect('borrower_list')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'books/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'books/add_category.html')

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('category_list')
    return render(request, 'books/edit_category.html', {'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category_list')