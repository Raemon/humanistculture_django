from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Song(models.Model):
    name = models.CharField(max_length=200)
    file = models.

    album = models.ForeignKey(Album)