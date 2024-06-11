from django.db import models

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
    