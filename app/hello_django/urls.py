from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from drf.urls import urlpatterns as drf_urls
urlpatterns = [
    path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path('news/', include('news.urls')),
    path('api_drf/', include(drf_urls)),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
