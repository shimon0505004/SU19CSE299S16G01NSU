from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detailsug', kwargs ={'pk': self.pk})


class Comment(models.Model):
	Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	Name = models.CharField(max_length=100)
	Email = models.EmailField(max_length=100)
	Body = models.TextField()
	Created = models.DateTimeField(default=timezone.now)
	Active = models.BooleanField(default=True)
	Parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')



# Create your models here.
