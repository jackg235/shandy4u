from django.db import models

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    style = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    brewer = models.CharField(max_length=200)
    abv = models.FloatField()
    bitterness = models.IntegerField()
    description = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " is a " + self.category + " brewed by " + self.brewer + " from " + self.country