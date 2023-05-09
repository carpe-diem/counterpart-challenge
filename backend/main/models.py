from django.db import models

class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('lat', 'lon')
