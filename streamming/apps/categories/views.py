from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

# Function-based home view (unchanged)
def home(request):
    return render(request, 'home.html', {})

# Class-based list category view
class CategoryListView(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})

# Class-based create category view
class CategoryCreateView(View):
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_category')
        return render(request, self.template_name, {'form': form})

# Class-based edit category view
class CategoryEditView(View):
    template_name = 'form.html'

    def get(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        form = CategoryForm(instance=category)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
        return render(request, self.template_name, {'form': form})

# Class-based delete category view
class CategoryDeleteView(View):
    template_name = 'delete.html'

    def get(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        return render(request, self.template_name, {'category': category})

    def post(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect('list_category')
