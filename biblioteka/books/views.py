from django.shortcuts import render, redirect, get_object_or_404
from .models import Borrower, Category

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