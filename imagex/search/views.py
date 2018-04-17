import os
from django.shortcuts import render
from .models import Image, Member, Category
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper


def index(request):
    all_images = Image.objects.all().order_by('-id')
    all_cat = Category.CATEGORY
    all_photog = Member.objects.all()
    return render(request, 'index.html', {'images': all_images, 'all_cat': all_cat, 'all_photog': all_photog})


def search_keyword(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)

        keywords = q.split(' ')
        if len(keywords) == 1:
            images = Image.objects.filter(tag__tag_name__iexact=keywords[0])
        else:
            # multiple keyword search: only show images containing all the tags

            images = Image.objects.filter(tag__tag_name__iexact=keywords[0])
            for k in keywords:
                images = images.filter(tag__tag_name__iexact=k)

        if len(request.GET.keys()) > 1:
            sort = request.GET.getlist('sort')[0]
            if sort == 'recent':
                images = images.order_by('-id')

        return render(request, 'search/results.html', {"q": q, "images": images,
                                                       'media_url': settings.MEDIA_URL})


def search_category(request):
    if request.method == 'GET':
        cat = request.GET.getlist('cat')[0]
        images = Image.objects.filter(category__exact=cat)

        if len(request.GET.keys()) > 1:
            sort = request.GET.getlist('sort')[0]
            if sort == 'recent':
                images = images.order_by('-id')

        d = dict(Category.CATEGORY)
        cat_name = d[cat]
        return render(request, 'search/category.html', {'cat_name': cat_name, 'images': images,
                                                        'media_url': settings.MEDIA_URL})


def search_photographer(request):
    if request.method == 'GET':
        photog = request.GET.getlist('photog')[0]
        images = Image.objects.filter(photographer__username__username__exact=photog)

        if len(request.GET.keys()) > 1:
            sort = request.GET.getlist('sort')[0]
            if sort == 'recent':
                images = images.order_by('-id')

        full_name = Member.objects.get(username=photog).username.first_name + " " + Member.objects.get(
            username=photog).username.last_name
        return render(request, 'search/photographer.html', {'full_name': full_name, 'images': images,
                                                            'media_url': settings.MEDIA_URL})


def download(request):
    if request.method == 'GET':
        img_name = list(request.GET.keys())[0]

        img_obj = Image.objects.get(img=img_name)
        img_obj.num_of_downloads += 1
        img_obj.save()

        filepath = os.path.join(settings.MEDIA_ROOT, img_name)
        wrapper = FileWrapper(open(filepath, 'rb'))
        response = HttpResponse(wrapper, content_type='image/jpeg')
        response['Content-Disposition'] = "attachment; filename=%s" % img_name
        return response
