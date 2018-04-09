from django.shortcuts import render
from account.models import Member
from search.models import Image, Tag
import datetime


def parse_tags(tag, img):
    data = tag.split(',')
    for d in data:
        if Tag.objects.filter(tagName__iexact=d).count() == 0:
            new_tag = img.tag.create(tagName=d)
        else:
            exist_tag = Tag.objects.filter(tagName__iexact=d)
            img.tag.add(exist_tag)


def upload_image(request):
    member = Member.objects.get(username=request.user.username)  # e.g. Member instance with username 'nat'
    all_cat = Image.CATEGORY
    message = state = ''
    d = datetime.date.today()
    daily_usage = str(4 - Image.objects.filter(uploadDate=d, photographer=member).count())
    system_usage = str(3 - Image.objects.filter(photographer=member).count())
    if request.method == 'POST':
        img_name = request.FILES.get('img').name
        tag_list = request.POST.get('tag').split(',')
        if len(tag_list) > 10:
            state = 'F'
            message = 'You cannot add more than 10 tags for an image. Please try again.'
        elif img_name.endswith(('.jpg', '.jpeg')):
            new_img = Image(
                img=request.FILES.get('img'),
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                category=request.POST.get('category'),
                photographer=member
            )
            new_img.save()

            # parse tags
            parse_tags(request.POST.get('tag'), new_img)

            # handle quota
            daily_usage = str(4 - Image.objects.filter(uploadDate=d, photographer=member).count())
            system_usage = str(3 - Image.objects.filter(photographer=member).count())

            # send success signal
            state = 'T'
            message = 'Image uploaded'
        else:
            # send error signal
            state = 'F'
            message = 'Image is not jpg. Please upload only jpg files.'
    return render(request, 'upload/upload.html', {'daily_usage': daily_usage, 'system_usage': system_usage, 'all_cat': all_cat, 'state': state, 'message': message})