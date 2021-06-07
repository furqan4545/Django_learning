from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # once u create something new from database u create this view where ur django will redirect u. so django will redirect u on detail page. 
        return reverse("basic_app:detail", kwargs = {'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()  # this field will only take positive values.
    school = models.ForeignKey(School, related_name = 'students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
# Now we will be registering these 2 dbs in admin.py file