from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

from django.shortcuts import render

def brand(request):
    return render(request, 'brand.html')

def model(request):
    return render(request, 'model.html')

def color(request):
    return render(request, 'color.html')