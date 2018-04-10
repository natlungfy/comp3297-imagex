from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
  path('',views.profile, name='view_profile'),
  path('<int:pk>/delete/',views.DeleteImage.as_view(), name='delete_image'),
]