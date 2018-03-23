from django.shortcuts import render
from search.models import Image


def index(request):
    # all_images = Image.objects.all()
    return render(request, 'search/index.html')


def results(request, keyword):
    images = Image.objects.filter(tag__icontains=keyword)
    # imagesid = ImageHasTag.objects.get(tagID=tagid)
    # images = Image.objects.filter(id=imagesid)
