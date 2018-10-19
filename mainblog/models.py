from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    """ Category models """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(null=True)
    text = models.TextField(null=True)
    is_archived = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='cover_images/')
    is_draft = models.BooleanField(default=False)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    @property
    def image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return sef.cover_image

    def __str__(self):
        return self.title
