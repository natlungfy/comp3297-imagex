from django.db import models
from account.models import Member
import datetime


class Image(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=90)
    CATEGORY = (
        ('ABS', 'Abstract'),
        ('AER', 'Aerial'),
        ('ANI', 'Animals'),
        ('ARC', 'Architecture'),
        ('BLA', 'Black and White'),
        ('FAM', 'Family'),
        ('FAS', 'Fashion'),
        ('FIN', 'Fine Art'),
        ('FOO', 'Food'),
        ('JOU', 'Journalism'),
        ('LAN', 'Landscape'),
        ('MAC', 'Macro'),
        ('NAT', 'Nature'),
        ('NIG', 'Night'),
        ('PEO', 'People'),
        ('PER', 'Performing Arts'),
        ('SPO', 'Sport'),
        ('STI', 'Still Life'),
        ('STR', 'Street'),
        ('TRA', 'Travel')
    )
    category = models.CharField(max_length=3, choices=CATEGORY, default='ABS')
    description = models.CharField(max_length=280)
    photographer = models.ForeignKey(Member, on_delete=models.CASCADE)
    uploadDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tagName = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.tagName


class ImageHasTag(models.Model):
    imgID = models.ManyToManyField(Image)
    tagID = models.ManyToManyField(Tag)

    def __str__(self):
        return self.imgID, self.tagID

