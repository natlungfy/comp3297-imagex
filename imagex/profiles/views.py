from django.shortcuts import render

from django.template import loader
from search.models import Image
from account.models import Member
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def profile(request):
    current_user_username = request.user.username
    current_user_pk = Member.objects.filter(username = current_user_username)[0].id
    users_images = Image.objects.filter(photographer=current_user_pk).order_by('-uploadDate', '-id')
    return render(request, 'profiles/profiles.html', {'images': users_images})    


 
