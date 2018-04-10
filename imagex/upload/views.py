from django.shortcuts import render
from account.models import Member
from search.models import Image, Tag, Category
import datetime


def parse_tags(tag, img):
    data = tag.split(',')
    for d in data:
        num_records = Tag.objects.filter(tag_name__iexact=d).count()
        if num_records == 0:
            img.tag.create(tag_name=d)
        else:
            exist_tag = Tag.objects.get(tag_name__iexact=d)
            img.tag.add(exist_tag)


def upload_image(request):
    member = Member.objects.get(username=request.user.username)  # e.g. Member instance with username 'nat'
    all_cat = Category.CATEGORY
    message = state = ''
    d = datetime.date.today()
    daily_usage = member.daily_quota
    if d > member.username.last_login.date():
        member.daily_quota = 4
        daily_usage = member.daily_quota
    system_usage = str(3 - Image.objects.filter(photographer=member).count())

    if request.method == 'POST':
        img_name = request.FILES.get('img').name
        tag_list = request.POST.get('tag').split(',')
        cat = Category.objects.get(cat_name=request.POST.get('category'))

        if len(tag_list) > 10:
            state = 'F'
            message = 'You cannot add more than 10 tags for an image. Please try again.'
        elif img_name.endswith(('.jpg', '.jpeg')):
            new_img = Image(
                img=request.FILES.get('img'),
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                category=cat,
                photographer=member
            )
            new_img.save()

            # parse tags
            parse_tags(request.POST.get('tag'), new_img)

            # handle quota
            member.daily_quota -= 1
            daily_usage = member.daily_quota
            system_usage = str(3 - Image.objects.filter(photographer=member).count())

            # send success signal
            state = 'T'
            message = 'Image uploaded'
        else:
            # send error signal
            state = 'F'
            message = 'Image is not jpg. Please upload only jpg files.'
    return render(request, 'upload/upload.html', {'daily_usage': daily_usage, 'system_usage': system_usage, 'all_cat': all_cat, 'state': state, 'message': message})