from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    username = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.username)
