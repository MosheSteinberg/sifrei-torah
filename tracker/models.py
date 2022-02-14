from django.db import models

# Create your models here.

class SeferTorah(models.Model):
    id=models.SmallIntegerField(primary_key=True)
    physical_location = models.TextField(choices=[
        ("Main", "Main Shul"),
        ("SY", "Shaar Yaakov"),
        ("Horowitz", "Horowitz"),
        ("YABM", "Yona Avraham")
        ]
    )