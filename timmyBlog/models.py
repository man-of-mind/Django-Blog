from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = CloudinaryField('image', null=True, blank=True)
    title_tag = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_post", blank=True)
    dislikes = models.ManyToManyField(User, related_name="blog", blank=True)
    
    def number_of_likes(self):
        return self.likes.count()


    def number_of_dislikes(self):
        return self.dislikes.count()


    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Anonymous")
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


    def get_absolute_url(self):
        return reverse('home')
