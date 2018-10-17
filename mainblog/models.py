from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=100, unique=True, null=True)
    description = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    date_mod = models.DateTimeField(null=True)
    text = models.TextField(null=True)
    is_archived = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='cover_images/')

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag")

    @property
    def image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return sef.cover_image

    def __str__(self):
        return self.title
