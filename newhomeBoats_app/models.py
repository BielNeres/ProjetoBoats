from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=25)
    country = models.CharField(max_length=25, default='Brasil')

    def __str__(self):
        return str(self.name) + " - " + str(self.country)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=25)
    nearby_cities = models.ManyToManyField('self', related_name="cities_nearby", blank=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Cities"
    
class IBGECityCodes(models.Model):
    ibge_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default="cidade")

    def __str__(self):
        return str(self.ibge_id) + " - " + str(self.name)
