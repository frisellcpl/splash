from django.contrib import admin

from splash.models import ImageBlock
from splash.models import Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title'],
    }


admin.site.register(ImageBlock)
admin.site.register(Page, PageAdmin)
