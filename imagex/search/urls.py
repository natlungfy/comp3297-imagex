from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex :: /search/nature/results/
    url(r'^results/$', views.results, name='results'),
]
