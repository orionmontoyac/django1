from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse(render(request, "core/home.html"))

def about(request):
    return HttpResponse(render(request, "core/about.html"))


def contact(request):
    return HttpResponse(render(request, "core/contact.html"))