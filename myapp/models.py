from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(unique=True, max_length=100, blank=False)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100, blank=False)
    url = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name
