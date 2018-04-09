from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^category/$', views.category, name='category'),
    url(r'^photographer/$', views.photographer, name='photographer'),
]
