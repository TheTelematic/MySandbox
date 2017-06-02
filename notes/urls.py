from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from notes import views, constants

urlpatterns = [
    url(constants.url_index, views.index, name='index'),
    url(constants.url_wall, views.wall, name='wall'),
    url(constants.url_register, views.register, name='register'),
    url(constants.url_aboutme, views.aboutme, name='aboutme'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
