from django.shortcuts import render, get_object_or_404 , redirect

from .models import Movies
from .forms import MoviesForm


def list_movie(request):
    movies = Movies.objects.all()
    return render(request, 'list_movie.html', {'movies': movies})

def create_movie(request):
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
    else:
        form = MoviesForm()
    return render(request, 'form_movie.html', {'form': form})

def edit_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    if request.method == "POST":
        form = MoviesForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
    else:
        form = MoviesForm(instance=movie)
    return render(request, 'form_movie.html', {'form': form})

def delete_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('list_movie')
    return render(request, 'delete_movie.html', {'movie': movie})
