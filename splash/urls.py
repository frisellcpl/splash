from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from splash import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug>[\w-]+)/$', views.home, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
