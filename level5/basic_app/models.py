from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    # If you want to add more fields to your default User class you need to write below line  i.e. one to one field 
    # this line is used when u want to add more fields to User builtin class, blc User model or user class allready have
    # username and lastname etc builtin. This line is used to add more fields.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional 
    portfolio_site = models.URLField(blank=True) # blank true mean that this field is optional

    profile_pic = models.ImageField(upload_to = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username
        # this will print username

    # after the database we need to create a form through which we will send the data. 



