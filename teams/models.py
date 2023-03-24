from django.db import models
from django.urls import reverse

class Team(models.Model):
    name = models.CharField(max_length=250)
    date_of_foundation = models.DateField(blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, default='default_logo.jpg')
    bio = models.TextField(null=True, blank=True)
    #coach
    country = models.CharField(max_length=70, db_index=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    titles = models.TextField(null=True, blank=True)
    players_amount = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Match(models.Model):
    team_home = models.ForeignKey(Team, blank=False, null=False, on_delete=models.CASCADE, related_name='team_home')
    team_away = models.ForeignKey(Team, blank=False, null=False, on_delete=models.CASCADE,  related_name='team_away')
    date = models.DateTimeField()
    tournament = models.CharField(max_length=200, blank=True, null=True)
    referee = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    finished = models.BooleanField(default=0)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f'{self.team_home} - {self.team_away}'


