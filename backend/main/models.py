from django.db import models

class City(models.Model):
    name = models.CharField(max_length=64)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name