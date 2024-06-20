"""
URL configuration for streamming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.categories.views import home, CategoryListView, CategoryCreateView, CategoryEditView, CategoryDeleteView
from apps.movies.views import MovieListView, MovieCreateView, MovieEditView, MovieDeleteView
from apps.trending.views import TrendingStarView , TrendingStarViewPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list_category/', CategoryListView.as_view(), name='list_category'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('edit_category/<int:id>/', CategoryEditView.as_view(), name='edit_category'),
    path('delete_category/<int:id>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('list_movies/', MovieListView.as_view(), name='list_movie'),
    path('create_movie/', MovieCreateView.as_view(), name='create_movie'),
    path('edit_movie/<int:id>/', MovieEditView.as_view(), name='edit_movie'),
    path('delete_movie/<int:id>/', MovieDeleteView.as_view(), name='delete_movie'),

    path('trending/', TrendingStarView.as_view(), name="trending_movies"),
    path('trending/star/<int:id>/', TrendingStarViewPost.as_view(), name="trending_star"),


]
