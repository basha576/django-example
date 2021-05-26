from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userinfo(models.Model):

    User = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    usersite=models.URLField(blank=True)
    user_profile=models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.User.username
#class userdata(models.Model):
