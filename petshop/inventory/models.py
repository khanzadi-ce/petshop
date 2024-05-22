from django.db import models

# Create your models here.
from django.db import models

class Species(models.Model):
    """
    Model for pet species (e.g., Dog, Cat, Bird)
    """
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Pet(models.Model):
    """
    Model for individual pets
    """
    species      = models.ForeignKey(Species, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100, blank=True)
    breed        = models.CharField(max_length=100, blank=True)
    age          = models.IntegerField(blank=True, null=True)
    description  = models.TextField(blank=True)
    image_url    = models.CharField(max_length=300, blank=True)
    stock        = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.species})"
