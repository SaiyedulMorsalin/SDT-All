from django.db import models

# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    CHOICES_RATE = [(1,1),(2,2),(3,3),(4,4),(5,5)]
    rating = models.IntegerField(choices=CHOICES_RATE)