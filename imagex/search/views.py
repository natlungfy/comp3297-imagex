from django.shortcuts import render
from .models import Image
from django.conf import settings


def index(request):
    all_images = Image.objects.all().order_by('-uploadDate', '-id')
    return render(request, 'index.html', {'images': all_images})


def results(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        images = Image.objects.filter(tag__icontains=keyword).order_by('-uploadDate', '-id')
        return render(request, 'search/results.html', {"keyword": keyword, "images": images,
                                                       'media_url': settings.MEDIA_URL})
