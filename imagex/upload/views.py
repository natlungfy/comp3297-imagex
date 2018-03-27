from django.shortcuts import render
from django.contrib import messages
from search.models import Image, Member


def uploadimg(request):
    member = Member.objects.get(username=request.user.username)  # Member instance with username 'nat'
    message = state = ''
    if request.method == 'POST':
        img_name = request.FILES.get('img').name
        if img_name.endswith(('.jpg', '.jpeg')):
            new_img = Image(
                img=request.FILES.get('img'),
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                category=request.POST.get('category'),
                tag=request.POST.get('tag'),
                photographer=member
            )
            new_img.save()
            # Decrease daily quota and system quota by one
            member.dailyQuota -= 1
            member.systemQuota -= 1
            member.save()
            state = 'T'
            message = 'Image uploaded'
        else:
            state = 'F'
            message = 'Image is not jpg. Please upload only jpg files.'
    return render(request, 'upload/upload.html', {'daily_quota': member.dailyQuota, 'system_quota': member.systemQuota, 'state': state, 'message': message})