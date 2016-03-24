from django.shortcuts import render

from splash.models import Page

def home(request, slug=None):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        page = Page.objects.all()[0]

    return render(request, 'home.html', {
        'page': page
    })
