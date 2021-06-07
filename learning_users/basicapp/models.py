from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) # this line is used when u want to add more fields to User builtin class, blc User model or user class allready have
    # username and lastname etc builtin. This line is used to add more fields. 

    # additional 
    portfolio_site = models.URLField(blank=True) # means not required. only optional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # upload_to tells pic storing path.this is a subdirectory in media folder.

    def __str__(self):
        return self.user.username