from django.shortcuts import render, HttpResponse

from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'core/core.html', {'projects': projects})

