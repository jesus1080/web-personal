from django.shortcuts import render
from .models import Project

# Create your views here.
# nos devuelve todos los objetos que tiene el modelo de proyecto 

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects}) 