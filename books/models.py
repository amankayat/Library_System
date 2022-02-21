from django.db import models

# Create your models here.


class book_data(models.Model):
    name = models.CharField(max_length=200)
    author= models.CharField(max_length=100)
    year = models.CharField(max_length=20)