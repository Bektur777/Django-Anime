from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import *
from .forms import ReviewForm


class AnimeView(ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)


class AnimeDetailView(DetailView):
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


class CharacterView(DetailView):
    model = Character
    template_name = 'anime/character.html'
    slug_field = 'name'
    context_object_name = 'character'
