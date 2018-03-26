from django.db import models
import datetime


class Member(models.Model):
    username = models.CharField(max_length=36, unique=True)
    password = models.CharField(max_length=36)
    name = models.CharField(max_length=70)
    dailyQuota = models.DecimalField(max_digits=1, decimal_places=0, default=4)
    systemQuota = models.DecimalField(max_digits=1, decimal_places=0, default=3)

    def __str__(self):
        return self.username


class Image(models.Model):
    img = models.ImageField(upload_to='images')
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
    tag = models.CharField(max_length=10, null=True)
    uploadDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
