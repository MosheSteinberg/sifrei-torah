from django.db import models

# Create your models here.

class OwnershipChoices(models.TextChoices):
    LOAN = "Loan", "Loan"
    OWNED = "Owned", "Owned"

class QualityChoices(models.TextChoices):
    TOP = 1, "First"
    SECOND = 2, "Second"
    THIRD = 3, "Third"
    DONTUSE = 4, "Don't Use"

class PhysicalLocation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Physical Location')

    def __str__(self):
        return self.name


class SeferTorah(models.Model):
    id=models.SmallIntegerField(primary_key=True)
    
    # Relevant people
    donator = models.CharField(max_length=100, default="Unknown")
    current_ownership = models.CharField(choices=OwnershipChoices.choices, max_length=10)

    # Locations
    physical_location = models.ForeignKey(PhysicalLocation, on_delete=models.PROTECT)

    # Practicals
    location_in_text = models.CharField(max_length=250, default="פרשת השבוע")
    quality = models.CharField(choices=QualityChoices.choices, max_length=10, default=QualityChoices.DONTUSE)

    picture = models.ImageField(blank=True)

    last_checked = models.DateField(null=True)
    donated = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Sifrei Torah"

    def __str__(self):
        return (str(self.id) + " - " + self.donator)


class SoferNotes(models.Model):
    sefer = models.ForeignKey(SeferTorah, on_delete=models.CASCADE)
    note = models.TextField()
    date_of_note = models.DateTimeField(auto_now_add=True, editable=False)