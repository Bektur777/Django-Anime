from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import *
from .forms import ReviewForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Anime.objects.filter(draft=False).values('year').distinct()


class AnimeView(ListView, GenreYear):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    paginate_by = 1


class AnimeDetailView(DetailView, GenreYear):
    model = Anime
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        anime = Anime.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.anime = anime
            form.save()
        return redirect(anime.get_absolute_url())


class CharacterView(DetailView, GenreYear):
    model = Character
    template_name = 'anime/character.html'
    slug_field = 'name'
    context_object_name = 'character'


class FilterAnimeView(ListView, GenreYear):
    paginate_by = 1

    def get_queryset(self):
        if 'genre' in self.request.GET and 'year' in self.request.GET:
            queryset = Anime.objects.filter(
                Q(year__in=self.request.GET.getlist("year")), Q(genres__in=self.request.GET.getlist("genre"))
            ).distinct()
        else:
            queryset = Anime.objects.filter(
                Q(year__in=self.request.GET.getlist("year")) | Q(genres__in=self.request.GET.getlist("genre"))
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join([f'year={x}&' for x in self.request.GET.getlist('year')])
        context['genre'] = ''.join([f'genre={x}&' for x in self.request.GET.getlist('genre')])
        return context