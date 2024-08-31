from django.db import models
from account.models import User
from django.utils.text import slugify

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="item/image")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)


STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    item =models.ForeignKey(Item,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.CharField(choices= STAR_CHOICES,max_length=10)
    created = models.DateTimeField(auto_now_add=True)
