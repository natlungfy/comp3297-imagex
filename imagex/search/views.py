import os
from django.shortcuts import render
from .models import Image, Member, Category
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.db.models import F
from django.shortcuts import redirect
from django.urls import reverse_lazy


def index(request):
    images = Image.objects.all()

    img_with_popularity = images.annotate(
        popularity=F('num_of_downloads') + F('num_of_likes')
    )

    all_images = img_with_popularity.order_by('-popularity')
    all_cat = Category.CATEGORY
    all_photog = Member.objects.all()
    return render(request, 'index.html', {'images': all_images, 'all_cat': all_cat, 'all_photog': all_photog})


def search_keyword(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        url_q = q.replace(' ', '+')
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
            elif sort == 'popular':
                img_with_popularity = images.annotate(
                    popularity=F('num_of_downloads') + F('num_of_likes')
                )
                images = img_with_popularity.order_by('-popularity')

        return render(request, 'search/results.html', {"q": q, "url_q": url_q, "images": images,
                                                       'media_url': settings.MEDIA_URL})


def search_category(request):
    if request.method == 'GET':
        cat = request.GET.getlist('cat')[0]
        images = Image.objects.filter(category__exact=cat)

        if len(request.GET.keys()) > 1:
            sort = request.GET.getlist('sort')[0]
            if sort == 'recent':
                images = images.order_by('-id')
            elif sort == 'popular':
                img_with_popularity = images.annotate(
                    popularity=F('num_of_downloads') + F('num_of_likes')
                )
                images = img_with_popularity.order_by('-popularity')
        else:
            img_with_popularity = images.annotate(
                popularity=F('num_of_downloads') + F('num_of_likes')
            )
            images = img_with_popularity.order_by('-popularity')

        d = dict(Category.CATEGORY)
        cat_name = d[cat]
        return render(request, 'search/category.html', {'q': cat, 'cat_name': cat_name, 'images': images,
                                                        'media_url': settings.MEDIA_URL})


def search_photographer(request):
    if request.method == 'GET':
        photog = request.GET.getlist('photog')[0]
        images = Image.objects.filter(photographer__username__username__exact=photog)

        if len(request.GET.keys()) > 1:
            sort = request.GET.getlist('sort')[0]
            if sort == 'recent':
                images = images.order_by('-id')
            elif sort == 'popular':
                img_with_popularity = images.annotate(
                    popularity=F('num_of_downloads') + F('num_of_likes')
                )
                images = img_with_popularity.order_by('-popularity')
        else:
            img_with_popularity = images.annotate(
                popularity=F('num_of_downloads') + F('num_of_likes')
            )
            images = img_with_popularity.order_by('-popularity')

        full_name = Member.objects.get(username=photog).username.first_name + " " + Member.objects.get(
            username=photog).username.last_name
        return render(request, 'search/photographer.html', {'q': photog, 'full_name': full_name, 'images': images,
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


def view_image(request):
    if request.method == 'GET':
        img_name = request.GET.get('img')

        img_obj = Image.objects.get(img=img_name)

        cat = dict(Category.CATEGORY)[img_obj.category.cat_name]
        return render(request, 'view_image.html', {'image': img_obj, 'cat': cat })


def like(request, pk):
    image = Image.objects.get(id=pk)
    image.num_of_likes += 1
    image.save()
    return redirect(reverse_lazy('profiles:view_profile', kwargs={'username': image.photographer.username}))
