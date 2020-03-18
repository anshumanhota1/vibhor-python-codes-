from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id': self.pk})
    """
        the above method is better then using {% url <url path> %}
        (vid ref 19 try django 1.9)
    """
    class Meta:
        ordering = ['-timestamp', '-last_updated']