from django.shortcuts import render, HttpResponse
from .models import Project


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()

    return HttpResponse(render(request, "portfolio/portfolio.html", {"projects":projects}))