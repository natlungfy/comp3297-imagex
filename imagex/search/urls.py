from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #ex :: /search/nature/results/
    path('char:keyword/results/', views.results, name='results')
]