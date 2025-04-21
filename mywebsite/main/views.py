from django.shortcuts import render
from django.http import HttpResponse

from .models import Game  # ✅ Correct if in the same app



def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})