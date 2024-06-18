from django.db import models
from musician.models import MusicianModel

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    # Defining choices for album_rating
    CHOICES_RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    album_rating = models.IntegerField(choices=CHOICES_RATING)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
