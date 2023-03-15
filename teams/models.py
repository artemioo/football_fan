from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=250)
    date_of_foundation = models.DateField(blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, default='default_logo.jpg')
    bio = models.TextField(null=True, blank=True)
    #coach
    country = models.CharField(max_length=70, db_index=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    titles = models.TextField(null=True, blank=True)
    players_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name