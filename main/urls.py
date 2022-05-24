from django.conf.urls.static import static
from django.urls import path
from core import settings
from main.views import MainPage, ProjectPage, AboutPage, PostDetail, ProjectDetail

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('post/<int:pk>', PostDetail.as_view(), name='detail_post'),
    path('projects', ProjectPage.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetail.as_view(), name='detail_project'),
    path('about', AboutPage.as_view(), name='about')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)