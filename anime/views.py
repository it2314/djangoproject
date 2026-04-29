from django.shortcuts import render

from django.http import HttpResponse

def anime_detail(request, name):
     from .models import Anime
     anime = Anime.objects.get(name=name)
     return render(request, "anime/detail.html", {"anime": anime})
 
def anime_homepage(request):
    return HttpResponse("testing")


def homepage(request):
     from .models import Anime
     animes = Anime.objects.all()
     return render(request, "anime/homepage.html", {"animes": animes})
