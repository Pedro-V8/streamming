from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Movies
from .forms import MoviesForm
from apps.trending.models import Trending


class MovieListView(View):
    template_name = 'list_movie.html'

    def get(self, request, *args, **kwargs):
        movies = Movies.objects.all()
        return render(request, self.template_name, {'movies': movies})


class MovieCreateView(View):
    template_name = 'form_movie.html'

    def get(self, request, *args, **kwargs):
        form = MoviesForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MoviesForm(request.POST)
        if form.is_valid():
            movie = form.save()
            trending_movie = Trending(movie=movie, star=False)
            trending_movie.save()
            return redirect('list_movie')
        return render(request, self.template_name, {'form': form})


class MovieEditView(View):
    template_name = 'form_movie.html'

    def get(self, request, id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=id)
        form = MoviesForm(instance=movie)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=id)
        form = MoviesForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
        return render(request, self.template_name, {'form': form})


class MovieDeleteView(View):
    template_name = 'delete_movie.html'

    def get(self, request, id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=id)
        return render(request, self.template_name, {'movie': movie})

    def post(self, request, id, *args, **kwargs):
        movie = get_object_or_404(Movies, id=id)
        Trending.objects.filter(movie=movie).delete()
        movie.delete()
        
        return redirect('list_movie')
