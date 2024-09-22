from django.shortcuts import render

def home(request):
    return render(request, 'action/home.html')

def profile(request):
    return render(request, 'action/profile.html')

def leaderboard(request):
    return render(request, 'action/leaderboard.html')

def settings(request):
    return render(request, 'action/settings.html')