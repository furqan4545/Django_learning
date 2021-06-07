from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# Here we will store blog post in db
class Post(models.Model):
    # Now i will introduce couple of fields here. 
    # here author is connected to super user on website. 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)  # u can adjust ur time zone in settings.py file by going and changing 'UTC'
    published_date = models.DateTimeField(blank= True, null = True)
    # it will be blank and null for instance blc we don't have know when the user will publish blog.

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # whenever I hit publish button it is gonna save the publishing date only at that time. Otherwise it will keep publishing date null.

    # then post can have comments on then so create another method.
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
        # so somewhere I would have a list of comments and some of them would be approved comments so I m gonna grab those approved comments. 

    def get_absolute_url(self):
        # after u done creating post and hit publish or save then where should I go. well go to post_detail page of the actual post which u created. 
        # passing in the primary key of the actual post. so u don't end up on someone else post. 
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    # foriegnkey tb use hoti hai jb ap ksi or model sy koi field uthaty ho ya phr pora model uthaty ho yani sari fields.
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')  # basicaly this line is going to connect each comment to actual post.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)  # this must match the above approved_comment arg in approve_comments method.

    def approve(self):
        self.approved_comment = True
        self.save

    # once a person is done writing comments he will be taken back to list of all the posts. i.e. he will get back to home page
    def get_absolute_url(self):
        # post_list is going to be our list view and we will use it as our homepage. 
        return reverse('post_list') 

    def __str__(self):
        return self.text

    
    

















