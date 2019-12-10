from django.contrib.auth.models import User
from django.db import models


# model for a drink/beer
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
    users = models.ManyToManyField(User, related_name='users')
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " is a " + self.category + " brewed by " + self.brewer + " from " + self.country

    def __eq__(self, other):
        return self.name == other.name

    def get_style(self):
        return self.style

    def get_category(self):
        return self.category

    def get_city(self):
        return self.city

    def get_website(self):
        return self.website

