from django.contrib import admin

from splash import models


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }

    exclude = (
        'primary_color',
        'secondary_text_color',
        'text_color'
    )


admin.site.register(models.IconBlock)
admin.site.register(models.SimpleBlock)
admin.site.register(models.ImageBlock)
admin.site.register(models.Page, PageAdmin)
