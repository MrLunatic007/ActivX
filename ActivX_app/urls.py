from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/profile', views.profile, name='profile'),
    path('/leaderboard', views.leaderboard, name='leaderboard'),
    path('/settings', views.settings, name='settings'),
]