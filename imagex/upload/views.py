from django.shortcuts import render
from upload.models import IMG


# Create your views here.
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
        	img = request.FILES.get('img'),
            title = request.POST.get('name'),
            description = request.POST.get('description'),
            category = request.POST.get('table')
        )
        new_img.save()
    return render(request, 'upload/uploadimg.html')

