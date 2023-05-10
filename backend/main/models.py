from django.db import models

class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('lat', 'lon')


class SearchHistory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    closest_earthquake = models.CharField(max_length=128)
    magnitude = models.FloatField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
