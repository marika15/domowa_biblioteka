from django.shortcuts import render, redirect, get_object_or_404
 
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