from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie, Person

class MovieList(ListView):
	model = Movie
	template_name = 'core/movies/list_view.html'
	paginate_by = 10

class MovieDetail(DetailView):
	# model = Movie
	template_name = 'core/movies/detail_view.html'
	queryset = (Movie.objects.all_with_related_persons())

class PersonDetail(DetailView):
	queryset = Person.objects.all_with_prefetch_movies()
	template_name = 'core/person/detail_view.html'

