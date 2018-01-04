from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    photo = models.URLField(blank=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('essays:post_detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('essays.Post')
    def __str__(self):
        return self.text[:20]