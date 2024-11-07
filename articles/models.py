from django.conf import settings
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "topic"
        verbose_name = "Topic"
        ordering = ["name"]

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
        db_table = 'article'
        verbose_name = 'Article'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Clap(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='claps'
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='claps'
    )
    count = models.IntegerField(default=1)  # Optional, in case you want multiple claps per user

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} clapped for {self.article} ({self.count} times)'