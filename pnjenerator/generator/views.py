from django.shortcuts import render
from django.utils.translation import activate


def index(request):
    activate('fr')
    return render(request, 'generator/index.html')

def npc(request):
    activate('fr')
    return render(request, 'generator/player.html')
