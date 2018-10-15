from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    date_mod = models.DateTimeField(null=True)
    text = models.TextField(null=True)
    #cover_image = models.ImageField(upload_to=)

    def __str__(self):
        return self.title



