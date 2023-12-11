from django.db import models

# Create your models here.
class Add_musician(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    Instrument_type = models.TextField()
    def __str__(self) -> str:
        return self.First_name
    