from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Message sent! You will soon receive a reply by email.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'home/index.html', context)


def branding(request):
    return render(request, "home/branding.html", {})


def website(request):
    return render(request, "home/website.html", {})


def illustration(request):
    return render(request, "home/illustration.html", {})


def terms(request):
    return render(request, "home/terms.html", {})
