from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Anime
from .forms import UserRatingForm, UserRegistrationForm, UserLoginForm

def homepage(request):
    animes = Anime.objects.all()
    return render(request, "anime/homepage.html", {"animes": animes})

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'anime/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'anime/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

def anime_detail(request, name):
    anime = get_object_or_404(Anime, name=name)
    ratings = anime.user_ratings.all()
    avg_rating = anime.average_user_rating()
    form = UserRatingForm(request.POST or None)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        if form.is_valid():
            rating = form.save(commit=False)
            rating.anime = anime
            rating.user = request.user
            rating.save()
            return redirect('anime_detail', name=anime.name)
    return render(request, "anime/detail.html", {
        "anime": anime,
        "ratings": ratings,
        "avg_rating": avg_rating,
        "form": form,
    })