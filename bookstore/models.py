from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    year=models.CharField(max_length=10)
