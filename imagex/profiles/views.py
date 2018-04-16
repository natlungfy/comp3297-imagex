from django.shortcuts import render
from search.models import Image
from accounts.models import Member

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
def profile(request):
    current_user_username = request.user.username
    current_user_pk = Member.objects.filter(username = current_user_username)[0].id
    users_images = Image.objects.filter(photographer=current_user_pk).order_by('-upload_date', '-id')
    return render(request, 'profiles/profiles.html', {'images': users_images})


class DeleteImage(DeleteView):
    model = Image
    success_url = reverse_lazy('profiles:view_profile')