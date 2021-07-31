from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.forms.utils import to_current_timezone


class Post(models.Model):
    blog_pic = models.ImageField(
        default='default.jpg', upload_to='blog_pics', blank=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
