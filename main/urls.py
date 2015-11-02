from django.conf.urls import include, url
from django.views.generic import TemplateView
from main import views


urlpatterns = [
    url(r'^$',  views.collage),
    url(r'^collage/', views.ready_collage),
]
