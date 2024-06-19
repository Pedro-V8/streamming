from django.shortcuts import render, get_object_or_404 , redirect

from .models import Category
from .forms import CategoryForm


def home(request):
    return render(request, 'home.html', {})

def list_category(request):
    categories = Category.objects.all()
    return render(request, 'list.html', {'categories': categories})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form})

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'form.html', {'form': form})

def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_category')  
    return render(request, 'delete.html', {'category': category})