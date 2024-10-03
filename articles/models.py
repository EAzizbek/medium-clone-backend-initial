from django.conf import settings
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('publish', 'Publish')], default='pending')
    topics = models.ManyToManyField('Topic', related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Article'

    def __str__(self):
        return self.title