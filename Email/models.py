from django.db import models

# Create your models here.

class Email(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    subject =models.CharField(max_length=150)
    message =models.TextField()
    time = models.DateTimeField(auto_now_add=True)
