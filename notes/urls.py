from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from notes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wall/$', views.wall, name='wall'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
