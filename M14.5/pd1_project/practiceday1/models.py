from django.db import models
from django.core.validators import validate_comma_separated_integer_list as comma_separated_validator
# Create your models here.
class PracticeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # autofield = models.AutoField()
    # bigautofield = models.BigAutoField()
    # bigintegerfield = models.BigIntegerField()
    # The line `# binaryfield = models.BinaryField()` is a commented-out line of code in a Django
    # model class. It is not active or used in the model definition.
    binaryfield = models.BinaryField()
    Check = models.BooleanField()
    feedback = models.CharField(max_length=255)
    comma = models.CharField(validators=[comma_separated_validator],max_length=200)
    date = models.DateField()
    datetime = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5,decimal_places=2)
    duration = models.DurationField()
    file = models.FileField(upload_to='files/')
    
    
    
    
    
    
    
    def __str__(self):
        return  self.name
    