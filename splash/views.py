from django.shortcuts import render

from splash.models import Page
from splash.models import PageIconBlock
from splash.models import PageSimpleBlock
from splash.models import PageImageBlock

def home(request, slug=None):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        page = Page.objects.all()[0]

    icon_blocks = PageIconBlock.objects.filter(page=page)
    simple_blocks = PageSimpleBlock.objects.filter(page=page)
    image_blocks = PageImageBlock.objects.filter(page=page)

    return render(request, 'home.html', {
        'page': page,
        'icon_blocks': icon_blocks,
        'simple_blocks': simple_blocks,
        'image_blocks': image_blocks,
    })
