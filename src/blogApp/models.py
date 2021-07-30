from django.db import models


class Blog(models.Model):
    blog_pic = models.ImageField(
        default='default.jpg', upload_to='blog_pics', blank=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
