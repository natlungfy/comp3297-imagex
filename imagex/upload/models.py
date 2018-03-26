from __future__ import unicode_literals
from django.db import models

CAT_CHOICES = (
	('math', 'MATH'),
	('art', 'ART'),
	('music', 'MUSIC'),
)
# Create your models here.
class IMG(models.Model):
	title = models.CharField(max_length = 50, null = True)
	img = models.ImageField(upload_to='upload')
	description = models.CharField(max_length = 200, null = True)
	category = models.CharField(max_length = 10, choices = CAT_CHOICES)