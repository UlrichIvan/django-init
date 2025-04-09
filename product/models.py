from django.contrib.gis.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector
import uuid6 as uuid
from django.contrib.gis.geos import Point


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    ref = models.CharField(max_length=255, unique=True, default=uuid.uuid6())
    description = models.TextField(default="")
    latitude = models.FloatField()
    longitude = models.FloatField()
    geolocation = models.PointField(srid=4326, geography=True, null=True)
    name_desc = SearchVectorField(verbose_name=["name", "description"])

    class Meta:
        indexes = [models.Index(fields=["name_desc"])]

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.geolocation = Point(self.latitude, self.longitude)
        if self.name and self.description:
            self.name_desc = SearchVector(self.name, self.description)
        super().save(*args, **kwargs)
