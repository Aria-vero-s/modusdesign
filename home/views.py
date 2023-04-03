from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, './home/index.html')


def branding(request):
    return render(request, "home/branding.html", {})


def website(request):
    return render(request, "home/website.html", {})


def illustration(request):
    return render(request, "home/illustration.html", {})
