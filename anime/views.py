from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Anime
from .forms import UserRatingForm

def homepage(request):
    animes = Anime.objects.all()
    return render(request, "anime/homepage.html", {"animes": animes})

def anime_detail(request, name):
    anime = get_object_or_404(Anime, name=name)
    ratings = anime.user_ratings.all()
    avg_rating = anime.average_user_rating()
    form = UserRatingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        rating = form.save(commit=False)
        rating.anime = anime
        rating.save()
        return redirect('anime_detail', name=anime.name)
    return render(request, "anime/detail.html", {
        "anime": anime,
        "ratings": ratings,
        "avg_rating": avg_rating,
        "form": form,
    })