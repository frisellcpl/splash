from django.contrib import admin

from splash import models

class IconBlockInline(admin.TabularInline):
    model = models.PageIconBlock
    extra = 0


class SimpleBlockInline(admin.TabularInline):
    model = models.PageSimpleBlock
    extra = 0


class ImageBlockInline(admin.TabularInline):
    model = models.PageImageBlock
    extra = 0

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }

    inlines = (
        ImageBlockInline,
        SimpleBlockInline,
        IconBlockInline,
    )

    exclude = (
        'primary_color',
        'secondary_text_color',
        'text_color'
    )


admin.site.register(models.IconBlock)
admin.site.register(models.SimpleBlock)
admin.site.register(models.ImageBlock)
admin.site.register(models.Page, PageAdmin)
