from django.shortcuts import render
from django.utils.translation import activate


def index(request):
    activate('fr')
    return render(request, 'generator/index.html')
