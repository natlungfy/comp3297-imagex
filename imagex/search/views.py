import os
from django.shortcuts import render
from .models import Image, Member, Category
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import mimetypes


def index(request):
    all_images = Image.objects.all().order_by('-upload_date', '-id')
    all_cat = Category.CATEGORY
    all_photog = Member.objects.all()
    return render(request, 'index.html', {'images': all_images, 'all_cat': all_cat, 'all_photog': all_photog})


def search_keyword(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        images = Image.objects.filter(tag__iexact=q).order_by('-upload_date', '-id')
        return render(request, 'search/results.html', {"q": q, "images": images,
                                                       'media_url': settings.MEDIA_URL})


def search_category(request):
    if request.method == 'GET':
        cat = list(request.GET.keys())[0]
        images = Image.objects.filter(category__exact=cat)
        d = dict(Category.CATEGORY)
        cat_name = d[cat]
        return render(request, 'search/category.html', {'cat_name': cat_name, 'images': images,
                                                       'media_url': settings.MEDIA_URL})


def search_photographer(request):
    if request.method == 'GET':
        photog = list(request.GET.keys())[0]
        images = Image.objects.filter(photographer__username__username__exact=photog)
        full_name = Member.objects.get(username=photog).username.first_name + " " + Member.objects.get(username=photog).username.last_name
        return render(request, 'search/photographer.html', {'full_name': full_name, 'images': images,
                                                       'media_url': settings.MEDIA_URL})


# def download(request):
#     if request.method == 'GET':
#         img_name = list(request.GET.keys())[0]
#         img = Image.objects.get(img=img_name)
#         wrapper = FileWrapper(open(img.img.file))  # img.file returns full path to the image
#         content_type = mimetypes.guess_type(img.img)[0]  # Use mimetypes to get file type
#         response = HttpResponse(wrapper,content_type=content_type)
#         response['Content-Length'] = os.path.getsize(img.img.file)
#         response['Content-Disposition'] = "attachment; filename=%s" % img.name
#         return response
