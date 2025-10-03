from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='posts/', default='construction.jpg')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False ,  blank=True)
    description = models.TextField(default='No description available.')
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
