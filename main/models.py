from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_cleanup import cleanup

@cleanup.select
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)
    full_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures')
    cover = models.ImageField(upload_to='cover_img')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})