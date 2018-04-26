from django.shortcuts import render
from search.models import Image
from accounts.models import Member
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import F

from django.urls import reverse_lazy


def edit_profile(request, username):
    if username == request.user.username:
        current_user_username = request.user.username
        current_user_pk = Member.objects.filter(username=current_user_username)[0].id
        member_description = Member.objects.filter(username=current_user_username)[0].description
        images = Image.objects.filter(photographer=current_user_pk)
        img_with_popularity = images.annotate(
            popularity=F('num_of_downloads') + F('num_of_likes')
        )
        users_images = img_with_popularity.order_by('-popularity')

        return render(request, 'profiles/profiles.html', {'images': users_images, 'member_description': member_description, 'member_pk': current_user_pk})


def update(request, pk):
    current_user_username = request.user.username
    member = Member.objects.get(username=current_user_username)

    member.description = request.POST.get('description')
    member.save(update_fields=["description"])

    request.user.first_name = request.POST.get('first_name')
    request.user.last_name = request.POST.get('last_name')
    request.user.email = request.POST.get('email')
    request.user.save(update_fields=['first_name', 'last_name', 'email'])

    return redirect(reverse_lazy('profiles:edit_profile', kwargs={'username': current_user_username}))


def view_profile(request, username):
    member_username = username
    current_user_pk = Member.objects.filter(username=member_username)[0].id
    member = User.objects.filter(username=username)[0]
    first_name = member.first_name
    last_name = member.last_name
    email = member.email
    member_description = Member.objects.filter(username=member_username)[0].description
    images = Image.objects.filter(photographer=current_user_pk)
    img_with_popularity = images.annotate(
        popularity=F('num_of_downloads') + F('num_of_likes')
    )
    users_images = img_with_popularity.order_by('-popularity')

    return render(request, 'profiles/member_profile.html',
                  {'images': users_images, 'username': member_username, 'member_description': member_description,
                   'member_pk': current_user_pk, 'first_name': first_name, 'last_name': last_name, 'email': email})


def delete(request, pk):
    current_user_username = request.user.username
    Image.objects.get(id=pk).delete()
    return redirect(reverse_lazy('profiles:edit_profile', kwargs={'username': current_user_username}))