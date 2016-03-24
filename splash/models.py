from django.db import models

from tinymce import models as tinymce_models


class ImageBlock(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    body = tinymce_models.HTMLField()
    image = models.ImageField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SimpleBlock(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.name


class IconBlock(SimpleBlock):
    icon = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    title = models.CharField(max_length=128)
    tagline = models.CharField(max_length=256, null=True, blank=True)
    quote = models.CharField(max_length=256, null=True, blank=True)

    primary_color = models.CharField(max_length=8, default='#595299')
    text_color = models.CharField(max_length=8, default='#4C4C4C')
    secondary_text_color = models.CharField(max_length=8, default='#FFFFFF')

    image_blocks = models.ManyToManyField(ImageBlock)
    simple_blocks = models.ManyToManyField(SimpleBlock)
    icon_blocks = models.ManyToManyField(IconBlock, related_name='icon_blocks')

    def __str__(self):
        return self.name
