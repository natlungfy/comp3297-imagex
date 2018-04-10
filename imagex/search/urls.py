from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^results/$', views.search_keyword, name='search_keyword'),
    url(r'^category/$', views.search_category, name='search_category'),
    url(r'^photographer/$', views.search_photographer, name='search_photographer'),
]
