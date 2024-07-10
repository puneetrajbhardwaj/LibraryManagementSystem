from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50,unique=True)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    availability_status = models.BooleanField(default=True)
