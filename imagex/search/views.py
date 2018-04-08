import os
from django.shortcuts import render
from .models import Image
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q


def index(request):
    all_images = Image.objects.all().order_by('-uploadDate', '-id')
    all_cat = Image.CATEGORY
    return render(request, 'index.html', {'images': all_images, 'all_cat': all_cat})


def results(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        images = Image.objects.filter(tag__iexact=q).order_by('-uploadDate', '-id')
        return render(request, 'search/results.html', {"q": q, "images": images,
                                                       'media_url': settings.MEDIA_URL})


def photographer(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        images = Image.objects.filter(Q(photographer__username__username__iexact=q) | Q(photographer__username__first_name__iexact=q) | Q(photographer__username__last_name__iexact=q)).order_by('-uploadDate', '-id')
        return render(request, 'search/photographer.html', {'q': q, 'images': images,
                                                       'media_url': settings.MEDIA_URL})


def category(request):
    if request.method == 'GET':
        cat_key = list(request.GET.keys())[0]
        images = Image.objects.filter(category__exact=cat_key)
        d = dict(Image.CATEGORY)
        cat_name = d[cat_key]
        return render(request, 'search/category.html', {'cat_name': cat_name, 'images': images,
                                                       'media_url': settings.MEDIA_URL})

#
# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404