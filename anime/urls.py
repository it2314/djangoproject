from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('anime/<str:name>/', views.anime_detail, name='anime_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
