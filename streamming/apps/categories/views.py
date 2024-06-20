from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

def home(request):
    return render(request, 'home.html', {})


class CategoryListView(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})


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


class CategoryDeleteView(View):
    template_name = 'delete.html'

    def get(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        return render(request, self.template_name, {'category': category})

    def post(self, request, id, *args, **kwargs):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect('list_category')
