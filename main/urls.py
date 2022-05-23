from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import settings
from main.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main'), # new
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)