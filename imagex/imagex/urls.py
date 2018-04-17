"""imagex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from search.views import download
from accounts.views import change_password
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^', include('search.urls')),
                  url(r'^login/$', auth_views.login, name="login"),
                  url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
                  path('search/', include('search.urls')),
                  path('admin/', admin.site.urls),
                  path('account/', include('allauth.urls')),
                  path('upload/', include('upload.urls')),
                  path('profiles/', include('profiles.urls')),
                  url(r'^download/$', download, name="download"),
                  url(r'^change_password/$', change_password, name='change_password'),
                  url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
                  url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      auth_views.password_reset_confirm, name='password_reset_confirm'),
                  url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
                  url(r'^invitations/', include('invitations.urls', namespace='invitations')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
