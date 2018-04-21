from django.db import models
from accounts.models import Member
import datetime


class Tag(models.Model):
    tag_name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.tag_name


class Category(models.Model):
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

    cat_name = models.CharField(max_length=3, choices=CATEGORY, default='ABS', unique=True)

    def __str__(self):
        return self.cat_name


class Image(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=90)
    category = models.ForeignKey(Category, to_field='cat_name', on_delete=models.CASCADE)
    description = models.CharField(max_length=280)
    tag = models.ManyToManyField(Tag)
    photographer = models.ForeignKey(Member, on_delete=models.CASCADE)
    upload_date = models.DateField(default=datetime.date.today)
    num_of_downloads = models.IntegerField(default=0)
    num_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
