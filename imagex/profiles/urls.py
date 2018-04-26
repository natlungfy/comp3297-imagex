from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
  path('<username>/edit', views.edit_profile, name='edit_profile'),
  path('<int:pk>/delete/', views.delete, name='delete_image'),
  path('<int:pk>/update/', views.update,name='update_profile'),
  path('<username>', views.view_profile, name='view_profile')
]
