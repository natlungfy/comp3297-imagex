from django.shortcuts import render
from search.models import Image
from accounts.models import Member
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.views.generic.edit import DeleteView,UpdateView
from django.urls import reverse_lazy


# Create your views here.
def profile(request):
    current_user_username = request.user.username
    current_user_pk = Member.objects.filter(username = current_user_username)[0].id
    member_description = Member.objects.filter(username = current_user_username)[0].description
    users_images = Image.objects.filter(photographer=current_user_pk).order_by('-upload_date', '-id')
    return render(request, 'profiles/profiles.html', {'images': users_images, 'member_description' : member_description, 'member_pk' : current_user_pk})

def update(request, pk):

    current_user_username = request.user.username
    current_user_pk = Member.objects.filter(username = current_user_username)[0].id
    member = Member.objects.filter(username = current_user_username)[0]
    users_images = Image.objects.filter(photographer=current_user_pk).order_by('-upload_date', '-id')
    
    member.description = request.POST.get('description')
    member.save(update_fields=["description"])
    member_description = Member.objects.filter(username = current_user_username)[0].description

    request.user.first_name = request.POST.get('first_name')
    request.user.last_name = request.POST.get('last_name')
    request.user.email = request.POST.get('email')
    request.user.save(update_fields=['first_name','last_name','email'])
    
    return redirect(reverse_lazy('profiles:view_profile'))


class DeleteImage(DeleteView):
    model = Image
    success_url = reverse_lazy('profiles:view_profile')

    
    
