from django.shortcuts import render
from account.models import Member
from search.models import Image, ImageHasTag, Tag
import datetime


def upload_image(request):
    member = Member.objects.get(username=request.user.username)  # e.g. Member instance with username 'nat'
    message = state = ''

    d = datetime.date.today()
    daily_usage = str(Image.objects.filter(uploadDate=d, photographer=member).count())
    system_usage = str(Image.objects.filter(photographer=member).count())
    if request.method == 'POST':
        img_name = request.FILES.get('img').name
        if img_name.endswith(('.jpg', '.jpeg')):
            new_img = Image(
                img=request.FILES.get('img'),
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                category=request.POST.get('category'),
                photographer=member
            )
            new_img.save()

            # parse tags: parse tag input from POST. Add it to Tag if it is a new tagName, then add the association in ImageHasTag.
            # parse_tags(request.POST.get('tag'))
            # tag_input=request.POST.get('tag')
            #
            # if Tag.objects.filter(tagName=tag_input).exists():
            #     new_assoc = ImageHasTag(imgID=new_img, tagID=Tag.objects.get(tagName=tag_input))
            # else:
            #     new_tag = Tag(tagName=tag_input)


            # handle quota
            daily_usage = str(Image.objects.filter(uploadDate=d, photographer=member).count())
            system_usage = str(Image.objects.filter(photographer=member).count())

            # send success signal
            state = 'T'
            message = 'Image uploaded'
        else:
            # send error signal
            state = 'F'
            message = 'Image is not jpg. Please upload only jpg files.'
    return render(request, 'upload/upload.html', {'daily_usage': daily_usage, 'system_usage': system_usage, 'state': state, 'message': message})