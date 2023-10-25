from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(null=True, validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    class TypeAnnonce(models.TextChoices):
        DISQUES = 'DISQUES'
        VETEMENTS = 'VÊTEMENTS'
        AFFICHES = 'AFFICHES'
        DIVERS = 'DIVERS'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    isSold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(default=2000, null=True, validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    type = models.fields.CharField(default=TypeAnnonce.DIVERS, choices=TypeAnnonce.choices, max_length=20)
    band = models.ForeignKey(Band, default='', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
