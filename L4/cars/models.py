from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} made in {self.year}"
