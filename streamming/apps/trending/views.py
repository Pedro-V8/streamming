from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Trending

class TrendingStarView(View):
    template_name = 'trending.html'

    def get(self, request, *args, **kwargs):
        
        trending_movies = Trending.objects.all().select_related('movie').order_by('-movie__release')
        context = {
            'trending_movies': trending_movies
        }
        return render(request, self.template_name, context)

class TrendingStarViewPost(View):
    template_name = 'trending.html'

    def get(self, request, *args, **kwargs):
        trending_movie = get_object_or_404(Trending, id=kwargs['id'])
        
        trending_movie.star = not trending_movie.star
        trending_movie.save()
        return redirect('trending_movies')