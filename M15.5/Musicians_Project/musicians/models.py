from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.last_name+" "+self.last_name}"