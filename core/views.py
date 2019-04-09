from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie

class MovieList(ListView):
	model = Movie
	template_name = 'core/movies/list_view.html'

class MovieDetail(DetailView):
	model = Movie
	template_name = 'core/movies/detail_view.html'

