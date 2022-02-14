from django.db import models

# Create your models here.

class PhysicalLocation(models.Model):
    name = models.CharField(max_length=200)


class SeferTorah(models.Model):
    id=models.SmallIntegerField(primary_key=True)
    physical_location = models.ForeignKey(PhysicalLocation)
    picture = models.ImageField()