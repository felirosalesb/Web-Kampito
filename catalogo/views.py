from django.shortcuts import render
from .models import Banner

# Create your views here.
def index(request):
    banners = Banner.objects.filter(activo=True)
    return render(request, 'catalogo/index.html', {'banners': banners})