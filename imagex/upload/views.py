from django.shortcuts import render
# from upload.models import IMG
from search.models import Image, Member


def uploadimg(request):
    # get member object, get member id, get their quota
    # in html, if quota > xxx, display disabled upload button, else display enabled upload button
    if request.method == 'POST':
        new_img = Image(
            img=request.FILES.get('img'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            tag=request.POST.get('tag'),
            photographer=Member.objects.get(id=request.POST.get('photographer'))
        )
        new_img.save()
    return render(request, 'upload/upload.html')
