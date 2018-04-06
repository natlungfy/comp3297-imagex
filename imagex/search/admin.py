from django.contrib import admin

from .models import Image, ImageHasTag, Tag

admin.site.register(Image)
admin.site.register(ImageHasTag)
admin.site.register(Tag)