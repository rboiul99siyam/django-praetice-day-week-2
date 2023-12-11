from django.db import models

# Create your models here.
from Musician.models import Add_musician
class add_album(models.Model):
    album_name = models.CharField(max_length=50)
    Album_release_date = models.DateTimeField()
    Album_rating = models.IntegerField()
    musician = models.ForeignKey(Add_musician, on_delete= models.CASCADE,default=None)
    def __str__(self) -> str:
        return self.album_name
    