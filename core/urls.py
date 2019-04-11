from django.urls import path

from .views import MovieList, MovieDetail, PersonDetail

app_name = 'core'
urlpatterns = [
	path('', MovieList.as_view(), name="movie_list"),
	path('<int:pk>', MovieDetail.as_view(), name="movie_detail"),
	path('person/<int:pk>', PersonDetail.as_view(),name='person_detail'),
]