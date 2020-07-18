from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class User_info(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio = models.URLField(blank = True)
    profile_pic = models.ImageField(blank = True,upload_to = 'profile_pics')


    def __str__(self):
        return self.user.username
